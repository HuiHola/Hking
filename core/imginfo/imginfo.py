import os 
import sys
import subprocess
path="$HOME/"+sys.argv[1]
output=subprocess.getoutput(f"exiftool {path}")
print(f"\033[92m    {output}\033[0m")
