#!/usr/bin/env python

# Tool name   :GetTrainInfo
# Module name :GetTrainInfo.py
# Detail      :The script to get Train information.
# Implementer :R.Ishikawa
# Version     :1.3
# Last update :2019/8/31

# Version History
# 1. Create New                                     R.I Ver.1.0  2019/4/1
# 2. Show only Train Delay information              R.I Ver.1.1  2019/5/24
# 3. Show all Train Delay Information of JR Line 
#    in Tokyo Metropolitan Area                     R.I Ver.1.2  2019/8/28
# 4. Divided DB to improve maintainability          R.I Ver.1.3  2019/8/31

from bs4 import BeautifulSoup as bs4
import urllib.request as ur
import re
import requests

# Read DB
senku_data = open("SENKU_DB.txt", "r")
url_data = open("URL_DB.txt", "r")

# Make DB SENKU List & URL List
SENKU_DB = senku_data.readlines()
URL_DB = url_data.readlines()

# Set Line Notify token and API
line_notify_token = 'INPUT YOUR TOKEN ID'
line_notify_api = 'https://notify-api.line.me/api/notify'

# Import Senku Data and URL from the beginning
for target_senku, url in zip(SENKU_DB, URL_DB):
    req = ur.urlopen(url)
    html = bs4(req, "html.parser")
    match = html.find(class_="corner_block_row_detail_d").string.replace('\n','')
    text = target_senku + '\n ' + match
            
    # Export only delay or cancel train information by using LINE Notify
    if match != '現在、平常通り運転しています。':
        message = '\n' + text
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + line_notify_token}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)

# Close DB
senku_data.close()
url_data.close()
