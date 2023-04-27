import cmd
import os
import subprocess

class img_info(cmd.Cmd):
    def __init__(self):
        self.path=""
        cmd.Cmd.__init__(self)
        self.prompt="\033[92mH-king@console \033[0m(\033[91mimginfo\033[0m) > "
    def do_help(self,args):
        print("\n")
        print("     path <imagepath>")
        print("")
        print("     run     for run")
    def do_clear(self,args):
        os.system("clear")
    def do_EOF(self,args):
        subprocess.getoutput("killall python *.py")
    def do_back(self,args):
        os.system("python img_info_back.py")
    def do_path(self,args):
        self.path="$HOME/"+args
        print(f"path => {self.path}")
    def do_run(self,args):
        if self.path != "":
            os.system(f"core/imginfo/imginfo.py {path}")
        else :
            print("     please set path of image")

try:
    img_info().cmdloop()
except KeyboardInterrupt as e:
    pass
