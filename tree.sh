#!/bin/sh

# Toolname    :tree.sh
# Detail      :The script to simulate windows command "tree".
# Implementer :R.Ishikawa
# Version     :1.0
# Last update :2017/10/02

#Version History
#1 Create New                   R.ishikawa    Ver.1.0

find . | sort | sed '1d;s/^\.//;s/\/\([^/]*\)$/|--\1/;s/\/[^/|]*/| /g' > filetree.txt
