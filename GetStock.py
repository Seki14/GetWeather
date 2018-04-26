##########################################################################
# Tool name   	:GetStock                                                #
# Module name   :GetStock.py                                             #
# Detail        :Script to obtain stock information from FRED.           #
#                https://fred.stlouisfed.org/                            #
# Implementer   :R.Ishikawa                                              #
# Version     	:1.3                                                     #
# Last update   :2018/4/26                                               #
##########################################################################

#Version History
#1 Create New                                                   2017/10/1   R.I    Ver.1.0
#2 Add Indices, NIKKEI225 and DJIA                              2017/12/10  R.I    Ver.1.1
#3 Add function to send gmail attached png file                 2018/2/24   R.I    Ver.1.2
#4 Be able to receive both JPN/USD and NIKKEI225/DJIA data      2018/4/26   R.I    Ver.1.3

#%matplotlib inline

import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
#3 import dateutil Module
from dateutil.relativedelta import relativedelta


#3 Add Function to send gmail #############################################
from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class sendGmailAttach:
    username, password = 'seki.ishikawa@gmail.com', 'seki14kawa'

    def __init__(self, to, sub, body, attach_file):
        host, port = 'smtp.gmail.com', 465
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to

        # mail main
        body = MIMEText(body)
        msg.attach(body)

        # Set Attachment
        attachment = MIMEBase('image', 'png')
        file = open(attach_file['path'], 'rb+')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        msg.attach(attachment)

        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()
        
#############################################################################

#3 Set data range automatically
today = datetime.datetime.today()
month_ago = today - relativedelta(months=1)

df = web.DataReader(["DEXJPUS"], "fred", month_ago, today)
df.plot()

plt.xlabel("Date")
plt.ylabel("Yen / Doller")
plt.savefig("JPNUSD.png", bbox_inches="tight")

#2 Add NIKKEI225 and DJIA Start
df2 = web.DataReader(["NIKKEI225", "DJIA"], "fred", month_ago, today)

df2.plot()

plt.xlabel("Date")
plt.ylabel("NIKKEI225/DJIA")
plt.savefig("NIKKEI225-DJIA.png", bbox_inches="tight")
#2 Add NIKKEI225 and DJIA End

#3 Add Main ##################################################################

if __name__ == '__main__':
    to = 'seki.ishikawa@gmail.com' # To:
    sub_JPNUSD = '[GetStock] Todays JPN/USD' #4 mail title for JPN/USD
    sub_NIKKEI225_DJIA = '[GetStock] Todays NIKKEI225-DJIA' #4 mail title for NIKKEI225-DJIA
    body = '' # body

    attach_file = {'name':'JPNUSD.png', 'path': '/Users/RyoISHIKAWA/Desktop/Code/tool/GetStock/JPNUSD.png'}
    
    #4 Add attached file, 'NIKKEI225-DJIA.png' start
    attach_file2 = {'name':'NIKKEI225-DJIA.png','path': '/Users/RyoISHIKAWA/Desktop/Code/tool/GetStock/NIKKEI225-DJIA.png'}
    #4 Add attached file, 'NIKKEI225-DJIA.png' end
    
    sendGmailAttach(to, sub_JPNUSD, body, attach_file)
    
    #4 Add sending precedure for NIKKEI225/DJIA start
    sendGmailAttach(to, sub_NIKKEI225_DJIA, body, attach_file2)
    #4 Add sending precedure for NIKKEI225/DJIA end

##############################################################################
