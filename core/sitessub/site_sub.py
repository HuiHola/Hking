#!/bin/bash/env python3

#import modules
import requests
import sys

#function for request to site
def subscanner(host,file):
    #open file
    with open(file,"r") as f:
        #read file line by line
        for line in f:
            #make domail suburl
            hostscanner=host+"/"+line
            try:
                #check request is 200 or not if is so url is showing
                if(requests.get(hostscanner)):
                    print("\033[32mactave: "+hostscanner+"\033[0m")
            except KeyboardInterrupt as e:
                #print(e)
                break

#get input diretct to file
host=sys.argv[1]

#try to read input file
try:
    path="$HOME"+sys.argv[2]
    subscanner(host,path)
except Exception as e: #if not file input so it's run
    subscanner(host,"../core/sitessub/dirbrute.txt")


