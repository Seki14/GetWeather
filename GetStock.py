##########################################################################
# Tool name   	:GetStock                                                #
# Module name   :GetStock.py                                             #
# Detail        :Script to obtain stock information from FRED.           #
#                https://fred.stlouisfed.org/                            #
# Implementer   :R.Ishikawa                                              #
# Version     	:1.2                                                     #
# Last update   :2018/2/24                                               #
##########################################################################

#Version History
#1 Create New                                    2017/10/1   R.I    Ver.1.0
#2 Add Indices, NIKKEI225 and DJIA               2017/12/10  R.I    Ver.1.1
#3 Add function to send gmail attached png file  2018/2/24   R.I    Ver.1.2

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
    username, password = 'XXXXXXXXXXXX@gmail.com', 'XXXXXXXXXXXXXX'

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
#df2 = web.DataReader(["NIKKEI225", "DJIA"], "fred", start, end)

#df2.plot()

#plt.xlabel("Date")
#plt.ylabel("NIKKEI225/DJIA")
#plt.savefig("NIKKEI225-DJIA.png", bbox_inches="tight")
#2 Add NIKKEI225 and DJIA End

#3 Add Main ##################################################################

if __name__ == '__main__':
    to = 'XXXXXXXXXXXXXXXX@gmail.com' # To:
    sub = '[GetStock] Todays JPN/USD' # mail title
    body = '' # body

    attach_file = {'name':'JPNUSD.png', 'path': '/Users/RI/Desktop/Code/tool/GetStock/JPNUSD.png'}
    sendGmailAttach(to, sub, body, attach_file)

##############################################################################
