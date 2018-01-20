#!/usr/bin/env python

# Tool name   :GetWeather
# Module name :GetWeather.py
# Detail      :The script to get weather information.
# Implementer :R.Ishikawa
# Version     :1.2
# Last update :2018/1/19

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0  2018/1/8
# 2. Add Line Notify functions          R.Ishikawa  Ver.1.1  2018/1/9
# 3. Add Description                    R.Ishikawa  Ver.1.2  2018/1/19

import urllib.request
from bs4 import BeautifulSoup

# Ver.1.1 START
import requests
line_notify_token = 'np2OIsiFIRKwOa2EgL8DJuZaJLeaPR83zEK9p5AZ0jR'
line_notify_api = 'https://notify-api.line.me/api/notify'
# Ver.1.1 END

# Get Weather Information (Default:Mito, Ibaraki, Japan)
rssurl = "http://weather.livedoor.com/forecast/rss/area/080010.xml"

tenki = []
# Ver.1.2 START
detail = []
# Ver.1.2 END

with urllib.request.urlopen(rssurl) as res:
    xml = res.read()
    soup = BeautifulSoup(xml, "html.parser")
    for item in soup.find_all("item"):
        title = item.find("title").string
        # Ver.1.2 START
        description = item.find("description").string
        # Ver.1.2 END
        if title.find("[ PR ]") == -1:
            tenki.append(title)
            # Ver.1.2 START
            detail.append(description)
            # Ver.1.2 END

for i in range(0,2):
    # Ver.1.1 START
    # print(tenki[i])
    # print(detail[i])
    message = tenki[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # Token
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    # Ver.1.1 END
    
    # Ver.1.2 START
    message2 = detail[i]
    payload2 = {'message': message2}
    headers2 = {'Authorization': 'Bearer ' + line_notify_token}  # Token
    line_notify2 = requests.post(line_notify_api, data=payload2, headers=headers2)
    # Ver.1.2 END

