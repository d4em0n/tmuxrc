import os
import sys

if len(sys.argv) < 2:
    exit()

home = os.getenv("HOME")
curdir = sys.argv[1].replace(home, " ~")
curdir = curdir.replace("/", "  ")
bgfg = "\033[38;5;233;48;5;192m"
normal = " \033[00m"
dircolor = bgfg+curdir+normal
print(dircolor)
