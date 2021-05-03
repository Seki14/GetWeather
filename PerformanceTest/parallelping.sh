#!/bin/sh

# Module:pararelping.sh
# Description:pingコマンドを複数回バックグラウンドで実行し、
#             ネットワーク負荷を上げるスクリプト。ネットワーク負荷試験で使用。
# Version: 1.1
# Implementer: Ryo Ishikawa

# Revision History
# 1. Create New   R.I ver.1.1

#ping実行先のIPアドレス
target=192.168.0.7
#並列実行数
para=100

for i in $(seq 1 $para)
do 
  ping -i 0.2 -s 1400 $target &
done

wait
