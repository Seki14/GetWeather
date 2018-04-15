#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tool name   :tree
# Module name :tree.py
# Detail      :The script to simulate Windows command "tree".
# Implementer :R.Ishikawa
# Version     :1.4
# Last update :2017/12/16

# Version History
# 1. Create New                           R.Ishikawa    Ver.1.0
# 2. display node, "|-"                   R.Ishikawa    Ver.1.1
# 3. Add messages                         R.Ishikawa    Ver.1.2
# 4. Changed node "|-" to "|__ "
#    Add "@" for directory                R.Ishikawa    Ver.1.3
# 5. Add shebang, messages & comments     R.Ishikawa    Ver.1.4

import os

# define export file
exportfile = "filetree.txt"

# define current directory
searchdir = "."

print ("\n"+"Export FileTree Start!")

# Scan directory and file
wk = os.walk(searchdir)

with open(exportfile,mode="w") as f:
    f.write("\n" + "'@' is directory." + "\n")
    f.write("FileTree is as follows... " + "\n" + "\n")
    
    for dirpath, dirs, files in wk:
        path = dirpath.split("/")
        # Export directory
        f.write("\t"*(len(path)-2) + "@" + " " + path[-1] + "\n")
        for x in files:
            #Export node and file
            f.write("\t"*(len(path)-1) + "|__" + " " + x + "\n")

print ("\n"+"Export FileTree Finished!"+"\n")
