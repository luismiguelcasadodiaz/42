#!/usr/bin/python3

import os
import sys

cwd = os.getcwd()
spiderpath = os.path.join(cwd, sys.argv[1])
try:
    if not os.path.isdir(spiderpath):  # spider path does not exist
        os.makedirs(spiderpath)          # then I create it
    else:                              # spider pathfolder exist
        if not os.access(spiderpath, os.W_OK):   # Check if folder allwos write
            msg = f"Write permission: i can not write inside {spiderpath}"
            raise ValueError(msg)

except PermissionError:
    msg = f"Write permission: can not create {spiderpath}"
    print(msg)
except ValueError as msg:
    print(msg)
