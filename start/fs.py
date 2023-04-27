import cmd
import os
import subprocess

class fs(cmd.Cmd):
    def __init__(self):
        self.host=''
        self.path=''
        cmd.Cmd.__init__(self)
        self.prompt='\033[92mH-king@console (\033[91msite_info/file_searcher\033[0m) > '
    def do_help(self,args):
        print('''
                        host <site domain>
                        \n
                        host https://example.com
                        \n
                        \n
                        path <path of txt file for file list> default is alrady set
                        \n
                        path <myfile.txt>

            ''')
    def do_EOF(self,args):
        subprocess.getoutput("killall python *.py")
    def do_clear(self,args):
        os.system("clear")
    def do_back(self,args):
        sys.exit(1)
    def do_host(self,args):
        self.host=args
        print(f"host => {self.host}")
    def do_path(self,args):
        self.path=args
        print(f"path => {self.path}")
    def do_run(self,args):
        if self.host != '' and self.path !='':
            os.system(f"python core/sitessub/site_sub.py {self.host} $HOME/{self.path}")
        elif self.host !='' and self.path =='':
            os.system(f"python core/sitessub/site_sub.py {self.host}")
        else :
            print("     some error please check host")

try:
    fs().cmdloop()
except KeyboardInterrupt as e:
    pass
