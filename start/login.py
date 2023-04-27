#!/bin/env pyton

#modules
import cmd
import sys
import random
import os
import subprocess
import random

##main code
#class inharit by cmd to make out own prompt

class prompt_command(cmd.Cmd):
    def __init__(self):
        #you can use super() here
        cmd.Cmd.__init__(self)
        self.prompt='\033[92mH-king@console \033[0m> '
        self.intro='            welcome to H-king console Home page\n              \033[91mctrl+d for exit\033[0m'
    def do_help(self,args):
        print(''' 
                    site_info   has many tools to get site info
                    
                    img_info    get information of image

                    phising_site    phising site
        ''')
    def do_EOF(self,args):
        subprocess.getoutput("killall python *.py")
    def do_clear(self,args):
        os.system("clear")
    def do_quit(self,args):
        sys.exit(1)
    #get site inof console
    def do_site_info(self,args):
       os.system("python start/site_info.py")
    def do_img_info(self,args):
        os.system("python3 start/img_info.py")
    def do_phising_site(self,args):
        os.system("python3 start/phising_came.py")
        

#this is for run
if __name__ == "__main__":
    try:
        try:
            aru=sys.argv[1]
            if aru=="q":
                prompt_command().cmdloop()
        except IndexError:
            idno=random.randint(1,5)
            os.system(f"cat start/bannder/id{idno}.txt")
            prompt_command().cmdloop()
    except KeyboardInterrupt:
        pass
