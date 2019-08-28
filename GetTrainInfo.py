#!/usr/bin/env python

# Tool name   :GetTrainInfo
# Module name :GetTrainInfo.py
# Detail      :The script to get Train information.
# Implementer :R.Ishikawa
# Version     :1.2
# Last update :2019/8/28

# Version History
# 1. Create New                                     R.I Ver.1.0  2019/4/1
# 2. Show only Train Delay information              R.I Ver.1.1  2019/5/24
# 3. Show all Train Delay Information of JR Line 
#    in Tokyo Metropolitan Area                     R.I Ver.1.2  2019/8/28

from bs4 import BeautifulSoup as bs4
import urllib.request as ur
import re
import requests

line_notify_token = 'W4lfg2BlQwceh6B1M2HqR4t9MLfmhJXKeZzVC55X83x'
line_notify_api = 'https://notify-api.line.me/api/notify'

SENKU_DB = ['【中央線快速電車(東京〜高尾)】',
            '【中央・総武各駅停車(三鷹〜千葉)】',
            '【中央本線(高尾〜小淵沢)',
            '【山手線】', 
            '【京浜東北線(大宮〜大船)】', 
            '【横須賀線(東京〜久里浜)】', 
            '【総武快速線(東京〜千葉)】', 
            '【東海道線(東京〜熱海)】', 
            '【常磐線(品川〜いわき)】', 
            '【常磐線快速電車(品川〜取手)】', 
            '【常磐線各駅電車(綾瀬〜取手)】', 
            '【宇都宮線(東京〜黒磯)】', 
            '【高崎線(東京〜高崎)】', 
            '【上野東京ライン】', 
            '【湘南新宿ライン】', 
            '【埼京線(大崎〜大宮)】', 
            '【南武線(川崎〜立川)】', 
            '【武蔵野線(府中本町〜西船橋)】', 
            '【青梅線(立川〜奥多摩)】', 
            '【五日市線(拝島〜武蔵五日市)】',
            '【横浜線(東神奈川〜八王子)】', 
            '【京葉線(東京〜蘇我)】'
            ]

URL_DB = ['http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_chuokaisoku',
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_chuosobu', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_chuo',
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_yamanote',
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_keihintohoku', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_yokosuka', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_sobukaisoku', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_tokaido', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_joban', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_jobankaisoku', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_jobankakueki', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_utsunomiya', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_takasaki', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_uenotokyo', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_shonanshinjuku', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_saikyo', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_nambu', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_musashino', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_ome', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_itsukaichi', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_yokohama', 
          'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_keiyo'
          ]


for target_senku, url in zip(SENKU_DB, URL_DB):
    req = ur.urlopen(url)
    html = bs4(req, "html.parser")
    match = html.find(class_="corner_block_row_detail_d").string.replace('\n','')
    text = target_senku + '\n ' + match
    if match != '現在、平常通り運転しています。':
        message = '\n' + text
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + line_notify_token}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)






