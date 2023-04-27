#/bin/env python3

import threading
import sys
import socket

try:
    site=sys.argv[1] #get domain name
    port_start=int(sys.argv[2]) #get start port
    port_end=int(sys.argv[3]) #get end port
except Exception as e:
    print(e)

# https://www.
#function for scanner
def get_ip(host):
    if (host[:12]=="https://www."):
        host=host.split("https://www.")
        host=host[1]
        ip=socket.gethostbyname(host)
    elif(host[:11]=="http://www."):
        host=host.split("http://www.")
        host=host[1]
        ip=socket.gethostbyname(host)
    elif(host[:4]=="www."):
        host=host.split("www.")[1]
        ip=socket.gethostbyname(host)
    else:
        ip=socket.gethostbyname(host)

    return ip

#get ip function
print(f"\n")
print(f"-------------------------------------------------")
print(f"\033[31mterget ip : \033[32m{get_ip(site)}\033[0m")
print(f"--------------------------------------------------")
print(f"\n")
#make port scanner
def port_scanner(site,ports):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #get ip of site
    host=get_ip(site)

    #create port connection
    try:
        socket.setdefaulttimeout(5)
        result=s.connect_ex((host,ports))
        if (result==0):
            print(f"\033[91mopen port : \033[92m{ports}")
    except KeyboardInterrupt as e :
        print("good by :)")
        sys.exit()
    except socket.gaierror:
        print("sorry host not be resulve")

for ports in range(port_start,port_end):
    port_scanner_runner=threading.Thread(target=port_scanner,args=(site,ports),daemon=True)
    port_scanner_runner.start()

