#!/bin/evm pyton

import os
import cmd
import sys
import subprocess

#own made module

#this is port scanner runner

class ps(cmd.Cmd):
    def __init__(self):
        self.host=""
        self.start_port=""
        self.end_port=""
        cmd.Cmd.__init__(self)
        self.prompt='\033[92mH-king@console\033[0m (\033[91msite_info/port_scanner\033[0m) > '
    def ps_runner(self,host,start,end):
        os.system(f"python3 core/port_scanner/scanner.py {host} {start} {end}")
    def do_help(self,args):
        print("         host <sitedomain>")
        print("")
        print("         host https://www.example.com")
        print ("")
        print ("")
        print ("        start_port <starting port>")
        print("")
        print("         start_port 1")
        print("")
        print("")
        print("         end_port <ending port>")
        print("")
        print("         end_port 1000")
        print("")
        print("         run")
        print("\033[91mnote: default is nothing\033[0m")
        print("")
        print("")

    def do_EOF(self,args):
        subrocess.getoutput("killall python *.py")
    def do_clear(self,args):
        os.system("clear")
    def do_back(self,args):
        sys.exit(1)
    def do_exit(self,args):
        os.system("exit")
    def do_host(self,args):
        if(args[:4]=="http"):
            self.host=args
            print(f"host => {self.host}")
        else:
            print("host is error")
    def do_start_port(self,args):
        try:
            self.start_port=int(args)
            print(f"start_port => {self.start_port}")
        except Exception as e:
            print("Enter a valid value")
    def do_end_port(self,args):
        try:
            self.end_port=int(args)
            print(f"end_port => {self.end_port}")
        except Exception as e:
            print("enter a valid value")
    def do_run(self,args):
        if(self.end_port !=""  and self.start_port !="" and self.host !=""):
            self.ps_runner(self.host,self.start_port,self.end_port)

try:        
    ps().cmdloop()
except KeyboardInterrupt as e:
    pass
