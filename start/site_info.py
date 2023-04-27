#!/bin/env python
#modules inbuilt
import cmd
import sys
import os
import subprocess

class site_info(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt="\033[92mH-king@console\033[0m (\033[91msite_info\033[0m) > "
    def do_help(self,args):
        print('''
                    port_scanner    scan the port and show open port
                    \n
                    \n
                    file_searcher    search the file list in host
        ''')
    def do_back(self,args):
        os.system("python login.py q ")
    def do_EOF(self,args):
        subprocess.getoutput("killall python *.py")
    #with this function we run port scanner but not directly
    def do_port_scanner(self,args):
        os.system("python start/ps.py")
    def do_file_searcher(self,args):
        os.system("python start/fs.py")
    def do_clear(self,arg):
        os.system("clear")
    def do_back(self,args):
        sys.exit(1)
    def do_exit(self,args):
        sys.exit(1)
try:
    site_info().cmdloop()
except KeyboardInterrupt as e:
    pass
