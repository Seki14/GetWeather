##########################################################################
# Tool name   	:ImportKakakuCOM                                         #
# Module name   :ImportKakakuCOM.py                                      #
# Detail        :Script to import Price infomation from Kakaku.COM       #
#                http://kakaku.com/                                      #
# Implementer   :R.Ishikawa                                              #
# Version     	:1.0                                                     #
# Last update   :2019/1/3                                                #
##########################################################################

#Version History
#1 Create New                                    2019/1/3   R.I    Ver.1.0

import requests
from bs4 import BeautifulSoup
import datetime

#path:出力先ディレクトリを入力（使用者が入力）
path = '/home/pi/Ryo/tools/ImportKakakuCOM/'
#date:タイムスタンプ(出力先ファイルに付与)
date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def scraping(url,outputfile):
   r = requests.get(url)
   soup = BeautifulSoup(r.text, "html.parser")
   with open(path + date + '_' + outputfile, mode='w') as f:
       for i in soup.find_all("a"):
           f.write(i.text) 

#####################################################################
#TV_url1,TV_outputfile1:TV売れ筋ランキングのURLと出力先txtファイル
#TV_url2,TV_outputfile2:TV注目ランキングのURLと出力先txtファイル
#TV_url3,TV_outputfile3:TV満足度ランキングのURLと出力先txtファイル

TV_url1 = "http://kakaku.com/kaden/lcd-tv/ranking_2041/"
TV_url2 = "http://kakaku.com/kaden/lcd-tv/ranking_2041/hot/"
TV_url3 = "http://kakaku.com/kaden/lcd-tv/ranking_2041/rating/"
TV_outputfile1 = 'TV_SalesRanking.txt'
TV_outputfile2 = 'TV_AttentionRanking.txt'
TV_outputfile3 = 'TV_SatisfactionRanking.txt'

scraping(TV_url1, TV_outputfile1)
scraping(TV_url2, TV_outputfile2)
scraping(TV_url3, TV_outputfile3)

#####################################################################
#WM_url1,WM_outputfile1:洗濯機売れ筋ランキングのURLと出力先txtファイル
#WM_url2,WM_outputfile2:洗濯機注目ランキングのURLと出力先txtファイル
#WM_url3,WM_outputfile3:洗濯機満足度ランキングのURLと出力先txtファイル

WM_url1 = "http://kakaku.com/kaden/vertical-washing/ranking_V042/"
WM_url2 = "http://kakaku.com/kaden/vertical-washing/ranking_V042/hot/"
WM_url3 = "http://kakaku.com/kaden/vertical-washing/ranking_V042/rating/"
WM_outputfile1 = 'WM_SalesRanking.txt'
WM_outputfile2 = 'WM_AttentionRanking.txt'
WM_outputfile3 = 'WM_SatisfactionRanking.txt'

scraping(WM_url1, WM_outputfile1)
scraping(WM_url2, WM_outputfile2)
scraping(WM_url3, WM_outputfile3)

#####################################################################
#RF_url1,RF_outputfile1:冷蔵庫売れ筋ランキングのURLと出力先txtファイル
#RF_url2,RF_outputfile2:冷蔵庫注目ランキングのURLと出力先txtファイル
#RF_url3,RF_outputfile3:冷蔵庫満足度ランキングのURLと出力先txtファイル

RF_url1 = "http://kakaku.com/kaden/freezer/ranking_2120/"
RF_url2 = "http://kakaku.com/kaden/freezer/ranking_2120/hot/"
RF_url3 = "http://kakaku.com/kaden/freezer/ranking_2120/rating/"
RF_outputfile1 = 'RF_SalesRanking.txt'
RF_outputfile2 = 'RF_AttentionRanking.txt'
RF_outputfile3 = 'RF_SatisfactionRanking.txt'

scraping(RF_url1, RF_outputfile1)
scraping(RF_url2, RF_outputfile2)
scraping(RF_url3, RF_outputfile3)

#####################################################################
