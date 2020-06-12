#!/usr/bin/env python

# Tool name   :GetWeather
# Module name :GetWeather.py
# Detail      :The script to get weather information.
# Implementer :R.Ishikawa
# Version     :1.6
# Last update :2020/6/12

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.0  2018/1/8
# 2. Add Line Notify functions          R.Ishikawa  Ver.1.1  2018/1/9
# 3. Add Description                    R.Ishikawa  Ver.1.2  2018/1/19
# 4. Add Weather icon                   R.Ishikawa  Ver.1.3  2018/8/17
# 5. Add 2 icons & delete old comments  R.Ishikawa  Ver.1.4  2018/10/23
# 6. Add URL notification               R.Ishikawa  Ver.1.5  2020/3/21
# 7. Implement refactoring              R.Ishikawa  Ver.1.6  2020/6/12 

import urllib.request
from bs4 import BeautifulSoup
import requests

# アイコンが格納されているパス（絶対パスで入力する）
icon_path = "/home/pi/Ryo/tools/GetWeather/"

line_notify_token = 'アクセストークンを入力してください'
line_notify_api = 'https://notify-api.line.me/api/notify'

# 抽出対象のRSSとURL(デフォルトは茨城県水戸市)
rssurl = "http://weather.livedoor.com/forecast/rss/area/080010.xml" 
URL = "http://weather.livedoor.com/area/forecast/080010"

tenki = []
detail = []

## Parser : 天気情報WebページのHTMLタグから天気情報を抽出してパースするメソッド ##########################
def Parser(rssurl):
   with urllib.request.urlopen(rssurl) as res:
      xml = res.read()
      soup = BeautifulSoup(xml, "html.parser")
      for item in soup.find_all("item"):
         title = item.find("title").string
         description = item.find("description").string
         if title.find("[ PR ]") == -1:
            tenki.append(title)
            detail.append(description)

## ck_Weather : 取得した天気情報とそれに応じたアイコンを出力するメソッド ################################
def ck_Weather(i, detail):
   if (detail[i].find("晴")) != -1 and (detail[i].find("曇")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open(icon_path + "Sun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                            
   elif (detail[i].find("晴時々曇")) != -1 or (detail[i].find("晴のち曇")) != -1:
       files = {'imageFile': open(icon_path + "SunToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                        
   elif (detail[i].find("晴時々雨")) != -1 or (detail[i].find("晴のち雨")) != -1:
       files = {'imageFile': open(icon_path + "SunToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                    
   elif (detail[i].find("晴時々雪")) != -1 or (detail[i].find("晴のち雪")) != -1:
       files = {'imageFile': open(icon_path + "SunToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                
   elif (detail[i].find("曇")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open(icon_path + "Cloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                            
   elif (detail[i].find("曇時々晴")) != -1 or (detail[i].find("曇のち晴")) != -1:
       files = {'imageFile': open(icon_path + "CloudToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                        
   elif (detail[i].find("曇時々雨")) != -1 or (detail[i].find("曇のち雨")) != -1:
       files = {'imageFile': open(icon_path + "CloudToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                    
   elif (detail[i].find("曇時々雪")) != -1 or (detail[i].find("曇のち雪")) != -1:
       files = {'imageFile': open(icon_path + "CloudToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                
   elif (detail[i].find("雨")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("曇")) == -1 and (detail[i].find("雪")) == -1:
       files = {'imageFile': open(icon_path + "Rain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                            
   elif (detail[i].find("雨時々晴")) != -1 or (detail[i].find("雨のち晴")) != -1:
       files = {'imageFile': open(icon_path + "RainToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                        
   elif (detail[i].find("雨時々曇")) != -1 or (detail[i].find("雨のち曇")) != -1:
       files = {'imageFile': open(icon_path + "RainToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                    
   elif (detail[i].find("雨時々雪")) != -1 or (detail[i].find("雨のち雪")) != -1:
       files = {'imageFile': open(icon_path + "RainToSnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                
   elif (detail[i].find("雪")) != -1 and (detail[i].find("晴")) == -1 and (detail[i].find("雨")) == -1 and (detail[i].find("曇")) == -1:
       files = {'imageFile': open(icon_path + "Snow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                            
   elif (detail[i].find("雪時々晴")) != -1 or (detail[i].find("雪のち晴")) != -1:
       files = {'imageFile': open(icon_path + "SnowToSun.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                                        
   elif (detail[i].find("雪時々曇")) != -1 or (detail[i].find("雪のち曇")) != -1:
       files = {'imageFile': open(icon_path + "SnowToCloud.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                                                                                                                                                                                                    
   elif (detail[i].find("雪時々雨")) != -1 or (detail[i].find("雪のち雨")) != -1:
       files = {'imageFile': open(icon_path + "SnowToRain.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
    
   elif (detail[i].find("暴風雨")) == -1:
       files = {'imageFile': open(icon_path + "Typhon.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)

   elif (detail[i].find("暴風雪")) == -1:
       files = {'imageFile': open(icon_path + "HeavySnow.png","rb")}
       line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)

   else:
       line_notify = requests.post(line_notify_api, data=payload, headers=headers)


## メイン処理 ###################################################################################

Parser(rssurl) # 天気予報サイトのHTMLタグから天気情報を抽出
for i in range(0,2):
    message = detail[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  

    ck_Weather(i, detail) # 天気情報とそれに応じた天気アイコンを出力

message = URL
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # Notify URL
line_notify = requests.post(line_notify_api, data=payload, headers=headers)

################################################################################################
