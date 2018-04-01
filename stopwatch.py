#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tool name   :stopwatch
# Module name :stopwatch.py
# Detail      :Simple stop watch to validate time performance.
# Implementer :R.Ishikawa
# Version     :1.0
# Last update :2018/04/01

# Version History
# 1. Create New                           R.Ishikawa    Ver.1.0

import time

print('\n########################################################')
print('################### STOPWATCH TOOL #####################')
print('########################################################\n')
    
print('If you push Enter, stopwatch is started.')
print('If you push Enter again after that, laptime is displayed.')
print('If you push Ctrl+C, stopwatch finish is finished')

input()
print('Start')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print('Lap #{}: {} ({})'.format(lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = now
        
except KeyboardInterrupt:
    # Ctrl+C procedure
    print("\nFinish.")
