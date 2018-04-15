#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tool name   :tree2
# Module name :tree2.py
# Detail      :The script to simulate Windows command "tree".
# Implementer :R.Ishikawa
# Version     :1.1
# Last update :2017/12/26

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0
# 2. Fix character corruption           R.Ishikawa  Ver.1.1

import os
import sys

if len(sys.argv) < 2:
    print('usage: ' + sys.argv[0] + ' <directory>')
    sys.exit(0)


flist = []
for root, dirs, files in os.walk(sys.argv[1]):
    root = os.path.relpath(root, sys.argv[1])
    if root == '.': root = ''
        
    flist.append([root, sorted(dirs), sorted(files)])


def print_file(filename,level_list,last):

    t = ''
        
    if len(level_list): t += ' '
        
    if len(level_list) >= 2:
          for b in level_list[1:]:
             if b:
                    t += ' '
             else:
                    t += '| '
    
    if len(level_list):
          if last:
             t += '|_ '
          else:
             t += '|- '


    print(t + filename)


def main(arg,level_list):
    root, dirs, files = arg
        
    dirlen = len(dirs)
    file_length = len(files)
    
    
    for i, dir_name in enumerate(dirs):
          nounder = (i == dirlen - 1 and file_length == 0)
                
          print_file('<' + dir_name + '>', level_list, nounder)
                
          under_root = os.path.join(root, dir_name)
          under_list = []
                
          for t in flist:
                if t[0] == under_root:
                     under_list.append(t)
                
          for j, t in enumerate(under_list):
                if nounder and j == len(under_list) - 1:
                     add = [True]
                else:
                     add = [False]
                        
                main(t, level_list + add)
        
    for i, filename in enumerate(files):
          print_file(filename, level_list, (i == file_length - 1))


main(flist.pop(0), [])
