#!/usr/bin/sh
# Script name:AutoGetWeather.sh
# Detail:The script to get weather information automatically.
# Implementer:R.Ishikawa
# Version:1.0
# Last update:2018/1/12

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0  2018/1/12

# Sleep Paramater
## 1min = 60 sec
##  1Hr = 3600 sec
## 12Hr = 43200 sec
## 24Hr = 86400 sec
 
while true
do
python /Users/RyoISHIKAWA/Desktop/Code/tool/GetWeather/GetWeather.py
echo "send message"
date
sleep 43200
done

