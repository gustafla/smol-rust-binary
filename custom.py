#!/usr/bin/env python
import sys
import subprocess

args = ["../smol/smold.py", "-m", "x86_64"]
out = str()
inp = list()
o = False
L = False

for arg in sys.argv:
    if o:
        out = arg
        o = False
        continue
    if L:
        args.append(arg)
        L = False
        continue
    if "custom.py" in arg:
        continue
    if arg.startswith("-W"):
        continue
    if arg.startswith("-nodefaultlibs"):
        continue
    if arg.startswith("-m"):
        continue
    if arg.startswith("-pie"):
        continue
    if arg.startswith("/"):
        inp.append(arg)
        continue
    if arg.startswith("-o"):
        o = True
        continue
    if arg.startswith("-L"):
        L = True

    args.append(arg)

args.extend(inp)
args.append(out)

for arg in args:
    print(arg)

run = subprocess.run(args)
exit(run.returncode)
