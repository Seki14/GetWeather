#! python3
# -*- coding: utf-8 -*-

# Tool name         :SpellChecker
# Module name       :SpellChecker.py
# Detail            :誤記、表記ゆれを検出するツールです。
# 　　　　 　　　　　　"退屈なことはPythonにやらせよう"付録Dの誤記検出ツールをベースにカスタマイズしたものです。　
#                     https://github.com/oreilly-japan/automatestuff-ja/tree/master/appendix-D
# Implementer       :R.Ishikawa
# Version           :1.0
# Last update       :2020/06/15

# HISTORY
#1 Create New        Ver.1.0  R.I  2020/06/15

import glob
import re
from collections import deque

import csv

print("\n")
print("#######################################")
print("############ SpellChecker #############")
print("#######################################\n")
print("誤記、表記ゆれを検出するツールです。\n")

# チェック対象のファイル名入力
target_file = input("チェック対象のファイル名称を入力してください:\n")

# 出力用CSVファイルを開く
csv_file = open('CheckResult.csv', 'a', newline="")
writer = csv.writer(csv_file)

token_re = re.compile(r'([一-龥]+|[A-Za-z][0-9A-Za-z_]*|[ァ-ヾ]+)')
token_pos = {}

for fname in glob.glob(target_file):
    writer.writerow(['語句', '検出された行数', '前の語句と出現頻度', '後の語句と出現頻度'])
    #print(fname)
    with open(fname, 'r', encoding='utf-8') as f:
        n = 0
        for line in f:
            n += 1
            if line.startswith('> ■') or line.startswith('・') or line.startswith('・・'):
                continue
            tokens = token_re.findall(line)
            for t in tokens:
                token_pos.setdefault(t, [])
                token_pos[t].append(fname + ':' + str(n))

last_tokens = deque([ ('', 0) ] * 3)

def push_and_print(t, length):
    last_tokens.popleft()
    last_tokens.append((t, length))
    if last_tokens[1][1] == 1:
        t1 = last_tokens[1][0]
        writer.writerow([t1, str(token_pos[t1][0]),str(last_tokens[0]), str(last_tokens[2])])
        #print(t1 + ',' + str(token_pos[t1][0]), end=',')
        #print(str(last_tokens[0]) + ',' + str(last_tokens[2]))
    
for t in sorted(token_pos.keys()):
    push_and_print(t, len(token_pos[t]))

push_and_print('', 0)