##########################################################################
# Tool name   	:ImportKakakuCOM                                         #
# Module name  :ImportKakakuCOM.py                                      #
# Detail       :Script to import Price infomation from Kakaku.COM       #
#               http://kakaku.com/                                      #
# Implementer  :R.Ishikawa                                              #
# Version     	:1.3                                                     #
# Last update  :2019/2/1                                               #
##########################################################################

#Version History
#1 Create New                                    2019/1/3   R.I    Ver.1.0
#2 Add mail sending function                     2019/1/5   R.I    Ver.1.1
#3 Add rel check about "a" tag                   2019/1/13  R.I    Ver.1.2
#4 Expand the number of attached file            2019/2/1   R.I    Ver.1.3

import requests
from bs4 import BeautifulSoup
import datetime

from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#path:出力先ディレクトリを入力（使用者が入力）
path = '/Users/Seki14/Desktop/Code/tool/ImportKakakuCOM/'
#date:タイムスタンプ(出力先ファイルに付与)
date = datetime.datetime.now().strftime('%Y%m%d%H%M')

#to:送信先メールアドレス
#sub:メールタイトル
#body:メール本文
to = 'mail@gmail.com'
sub = '【' + datetime.datetime.now().strftime('%m/%d')+ '】' + '価格.comのランキング情報'
body = ''

### scraping:指定したURLから抽出したいHTMLタグの情報を抽出する関数 ##########
def scraping(url,outputfile):
   r = requests.get(url)
   soup = BeautifulSoup(r.text, "html.parser")
   with open(path + date + '_' + outputfile, mode='w') as f:
       for i in soup.find_all("a", href=True, rel=lambda x: "nofollow" not in str(x).lower()):
           f.write(i.text)
           
### sendGmailAttatch:出力ファイルを添付してメール送信するクラス ############
class sendGmailAttach:
    username, password = 'mail@gmail.com', 'yourpassward'

    def __init__(self, to, sub, body, attach_file, attach_file2,attach_file3, attach_file4, attach_file5, attach_file6, attach_file7, attach_file8, attach_file9, attach_file10, attach_file11, attach_file12):
        host, port = 'smtp.gmail.com', 465
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to

        ### mail main###################################################################################
        body = MIMEText(body)
        msg.attach(body)

        ### Set Attachment ########################################################################
        attachment1 = MIMEBase('image', 'png')
        file = open(attach_file['path'], 'rb+')
        attachment1.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment1)
        attachment1.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        msg.attach(attachment1)

        attachment2 = MIMEBase('image', 'png')
        file = open(attach_file2['path'], 'rb+')
        attachment2.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment2)
        attachment2.add_header("Content-Disposition", "attachment", filename=attach_file2['name'])
        msg.attach(attachment2)

        attachment3 = MIMEBase('image', 'png')
        file = open(attach_file3['path'], 'rb+')
        attachment3.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment3)
        attachment3.add_header("Content-Disposition", "attachment", filename=attach_file3['name'])
        msg.attach(attachment3)

        attachment4 = MIMEBase('image', 'png')
        file = open(attach_file4['path'], 'rb+')
        attachment4.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment4)
        attachment4.add_header("Content-Disposition", "attachment", filename=attach_file4['name'])
        msg.attach(attachment4)

        attachment5 = MIMEBase('image', 'png')
        file = open(attach_file5['path'], 'rb+')
        attachment5.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment5)
        attachment5.add_header("content-Disposition", "attachment", filename=attach_file5['name'])
        msg.attach(attachment5)

        attachment6 = MIMEBase('image', 'png')
        file = open(attach_file6['path'], 'rb+')
        attachment6.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment6)
        attachment6.add_header("content-Disposition", "attachment", filename=attach_file6['name'])
        msg.attach(attachment6)

        attachment7 = MIMEBase('image', 'png')
        file = open(attach_file7['path'], 'rb+')
        attachment7.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment7)
        attachment7.add_header("Content-Disposition", "attachment", filename=attach_file7['name'])
        msg.attach(attachment7)

        attachment8 = MIMEBase('image', 'png')
        file = open(attach_file8['path'], 'rb+')
        attachment8.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment8)
        attachment8.add_header("Content-Disposition", "attachment", filename=attach_file8['name'])
        msg.attach(attachment8)

        attachment9 = MIMEBase('image', 'png')
        file = open(attach_file9['path'], 'rb+')
        attachment9.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment9)
        attachment9.add_header("Content-Disposition", "attachment", filename=attach_file9['name'])
        msg.attach(attachment9)

        attachment10 = MIMEBase('image', 'png')
        file = open(attach_file10['path'], 'rb+')
        attachment10.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment10)
        attachment10.add_header("Content-Disposition", "attachment", filename=attach_file10['name'])
        msg.attach(attachment10)

        attachment11 = MIMEBase('image', 'png')
        file = open(attach_file11['path'], 'rb+')
        attachment11.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment11)
        attachment11.add_header("Content-Disposition", "attachment", filename=attach_file11['name'])
        msg.attach(attachment11)

        attachment12 = MIMEBase('image', 'png')
        file = open(attach_file12['path'], 'rb+')
        attachment12.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment12)
        attachment12.add_header("Content-Disposition", "attachment", filename=attach_file12['name'])
        msg.attach(attachment12)

        ############################################################################################
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()
        #################################################################################################


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
#RC_url1,RC_outputfile1:炊飯器売れ筋ランキングのURLと出力先txtファイル
#RC_url2,RC_outputfile2:炊飯器注目ランキングのURLと出力先txtファイル
#RC_url3,RC_outputfile3:炊飯器満足度ランキングのURLと出力先txtファイル

RC_url1 = "http://kakaku.com/kaden/rice-cooker/ranking_2125/"
RC_url2 = "http://kakaku.com/kaden/rice-cooker/ranking_2125/hot/"
RC_url3 = "https://kakaku.com/kaden/rice-cooker/ranking_2125/rating/"
RC_outputfile1 = 'RC_SalesRanking.txt'
RC_outputfile2 = 'RC_AttentionRanking.txt'
RC_outputfile3 = 'RC_SatisfactionRanking.txt'

scraping(RC_url1, RC_outputfile1)
scraping(RC_url2, RC_outputfile2)
scraping(RC_url3, RC_outputfile3)

#####################################################################

attach_file = {'name':TV_outputfile1, 'path': path+date+'_'+TV_outputfile1}
attach_file2 = {'name':TV_outputfile2, 'path': path+date+'_'+TV_outputfile2}
attach_file3 = {'name':TV_outputfile3, 'path': path+date+'_'+TV_outputfile3}

attach_file4 = {'name':WM_outputfile1, 'path': path+date+'_'+WM_outputfile1}
attach_file5 = {'name':WM_outputfile2, 'path': path+date+'_'+WM_outputfile2}
attach_file6 = {'name':WM_outputfile3, 'path': path+date+'_'+WM_outputfile3}

attach_file7 = {'name':RF_outputfile1, 'path': path+date+'_'+RF_outputfile1}
attach_file8 = {'name':RF_outputfile2, 'path': path+date+'_'+RF_outputfile2}
attach_file9 = {'name':RF_outputfile3, 'path': path+date+'_'+RF_outputfile3}

attach_file10 = {'name':RC_outputfile1, 'path': path+date+'_'+RC_outputfile1}
attach_file11 = {'name':RC_outputfile2, 'path': path+date+'_'+RC_outputfile2}
attach_file12 = {'name':RC_outputfile3, 'path': path+date+'_'+RC_outputfile3}

sendGmailAttach(to, sub, body, attach_file, attach_file2, attach_file3, attach_file4, attach_file5, attach_file6, attach_file7, attach_file8, attach_file9, attach_file10, attach_file11, attach_file12)
