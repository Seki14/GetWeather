#!/usr/bin/env python

# Tool name   :GetWeather
# Module name :GetWeather.py
# Detail      :The script to get weather information.
# Implementer :R.Ishikawa
# Version     :1.1
# Last update :2018/1/9

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0  2018/1/8
# 2. Add Line Notify functions          R.Ishikawa  Ver.1.1  2018/1/9

import urllib.request
from bs4 import BeautifulSoup

# Ver.1.1 START
import requests
line_notify_token = 'ACCCESS TOKEN NAME'
line_notify_api = 'https://notify-api.line.me/api/notify'
# Ver.1.1 END

# Get Weather Information (Default:Mito, Ibaraki, Japan)
rssurl = "http://weather.livedoor.com/forecast/rss/area/080010.xml"

tenki = []
with urllib.request.urlopen(rssurl) as res:
    xml = res.read()
    soup = BeautifulSoup(xml, "html.parser")
    for item in soup.find_all("item"):
        title = item.find("title").string
        if title.find("[ PR ]") == -1:
            tenki.append(title)

for i in range(0,2):
    # Ver.1.1 START
    # print(tenki[i])
    message = tenki[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # Token
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    # Ver.1.1 END
