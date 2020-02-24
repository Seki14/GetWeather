##########################################################################
# Tool name   	:GetStock                                                #
# Module name   :GetStock.py                                             #
# Detail        :Script to obtain stock information from FRED.           #
#                https://fred.stlouisfed.org/                            #
# Implementer   :R.Ishikawa                                              #
# Version     	:1.4                                                     #
# Last update   :2020/2/24                                               #
##########################################################################

#Version History
#1 Create New                                                   2017/10/1   R.I    Ver.1.0
#2 Add Indices, NIKKEI225 and DJIA                              2017/12/10  R.I    Ver.1.1
#3 Add function to send gmail attached png file                 2018/2/24   R.I    Ver.1.2
#4 Be able to receive both JPN/USD and NIKKEI225/DJIA data      2018/4/26   R.I    Ver.1.3
#5 Chagne mail notify to LINE Notify                            2020/2/24   R.I    Ver.1.4

#%matplotlib inline

import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import requests

# Set data range automatically
today = datetime.datetime.today()
month_ago1 = today - relativedelta(months=1)
month_ago2 = today - relativedelta(months=2)

# DEXJPUS Start (DISABLE)
#df = web.DataReader(["DEXJPUS"], "fred", month_ago2, today)
#df.plot()

#plt.xlabel("Date")
#plt.ylabel("Yen / Doller")
#plt.savefig("JPNUSD.png", bbox_inches="tight")
# DEXJPUS End

# DJIA Start (DISABLE)
#df2 = web.DataReader(["DJIA"], "fred", month_ago1, today)
#df2.plot()

#plt.xlabel("Date")
#plt.ylabel("DJIA")
#plt.savefig("DJIA.png", bbox_inches="tight")
# DJIA End

# NIKKEI225 Start
df3 = web.DataReader(["NIKKEI225"], "fred", month_ago2, today)
df3.plot()

plt.xlabel("Date")
plt.ylabel("NIKKEI225")
plt.savefig("NIKKEI225.png", bbox_inches="tight")

# NIKKEI225 End

# Execute LINE NOTIFY ########################################################

line_notify_token = 'LINE_NOTIFY_TOKEN'
line_notify_api = 'https://notify-api.line.me/api/notify'

#message = '\n' + "(1)ドル円相場" + '\n' + "(2)ダウ平均株価" + '\n' + "(3)日経平均株価"
message = today.strftime('%m/%d') + "時点の日経平均株価"
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}

#files = {'imageFile': open("/home/pi/Ryo/tools/GetStock/JPNUSD.png","rb")}
#files2 =  {'imageFile': open("/home/pi/Ryo/tools/GetStock/DJIA.png","rb")}
files3 =  {'imageFile': open("/home/pi/Ryo/tools/GetStock/NIKKEI225.png","rb")}

#line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
#line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files2)
line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files3)

##############################################################################
