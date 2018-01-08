#!/usr/bin/env python

# Tool name   :GetWeather
# Module name :GetWeather.py
# Detail      :The script to get weather information.
# Implementer :R.Ishikawa
# Version     :1.0
# Last update :2018/1/8

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0

import urllib.request
from bs4 import BeautifulSoup

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

for i in range(0,8):
   print(tenki[i])
