#!/usr/bin/env python

# Tool name   :GetWeather
# Module name :GetWeather.py
# Detail      :The script to get weather information.
# Implementer :R.Ishikawa
# Version     :1.5
# Last update :2020/3/21

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0  2018/1/8
# 2. Add Line Notify functions          R.Ishikawa  Ver.1.1  2018/1/9
# 3. Add Description                    R.Ishikawa  Ver.1.2  2018/1/19
# 4. Add Weather icon                   R.Ishikawa  Ver.1.3  2018/8/17
# 5. Add 2 icons & delete old comments  R.Ishikawa  Ver.1.4  2018/10/23
# 6. Add URL notification               R.Ishikawa  Ver.1.5  2020/3/21

import urllib.request
from bs4 import BeautifulSoup
import requests

line_notify_token = 'INPUT YOUR TOKEN ID'
line_notify_api = 'https://notify-api.line.me/api/notify'

# Get Weather Information (Default:Mito, Ibaraki, Japan)
rssurl = "http://weather.livedoor.com/forecast/rss/area/080010.xml"

tenki = []
detail = []

with urllib.request.urlopen(rssurl) as res:
    xml = res.read()
    soup = BeautifulSoup(xml, "html.parser")
    for item in soup.find_all("item"):
        title = item.find("title").string
        description = item.find("description").string

        if title.find("[ PR ]") == -1:
            tenki.append(title)
            detail.append(description)


for i in range(0,2):
    message = detail[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # Notify Weather Info & Icon.
    
    if (detail[i].find("晴")) != -1 and (detail[i].find("曇")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/Sun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                            
    elif (detail[i].find("晴時々曇")) != -1 or (detail[i].find("晴のち曇")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SunToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                        
    elif (detail[i].find("晴時々雨")) != -1 or (detail[i].find("晴のち雨")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SunToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                    
    elif (detail[i].find("晴時々雪")) != -1 or (detail[i].find("晴のち雪")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SunToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                
    elif (detail[i].find("曇")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/Cloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                            
    elif (detail[i].find("曇時々晴")) != -1 or (detail[i].find("曇のち晴")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/CloudToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                        
    elif (detail[i].find("曇時々雨")) != -1 or (detail[i].find("曇のち雨")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/CloudToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                    
    elif (detail[i].find("曇時々雪")) != -1 or (detail[i].find("曇のち雪")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/CloudToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                
    elif (detail[i].find("雨")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("曇")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/Rain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                            
    elif (detail[i].find("雨時々晴")) != -1 or (detail[i].find("雨のち晴")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/RainToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                        
    elif (detail[i].find("雨時々曇")) != -1 or (detail[i].find("雨のち曇")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/RainToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                    
    elif (detail[i].find("雨時々雪")) != -1 or (detail[i].find("雨のち雪")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/RainToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                
    elif (detail[i].find("雪")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("曇")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/Snow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                            
    elif (detail[i].find("雪時々晴")) != -1 or (detail[i].find("雪のち晴")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SnowToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                                        
    elif (detail[i].find("雪時々曇")) != -1 or (detail[i].find("雪のち曇")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SnowToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                                                    
    elif (detail[i].find("雪時々雨")) != -1 or (detail[i].find("雪のち雨")) != -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/SnowToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
    
    elif (detail[i].find("暴風雨")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/Typhon.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)

    elif (detail[i].find("暴風雪")) == -1:
       files = {'imageFile': open("/home/pi/Ryo/tools/GetWeather/HeavySnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)

    else:
       line_notify = requests.post(line_notify_api, data=payload, headers=headers)

message = rssurl
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # Notify URL
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
