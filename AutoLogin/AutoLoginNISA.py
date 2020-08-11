#!/usr/bin/env python

# Tool name   :AutoLoginNISA
# Module name :AutoLoginNISA.py
# Detail      :楽天証券のマイページへ自動ログインするためのスクリプト
# Implementer :R.Ishikawa
# Version     :1.1
# Last update :2020/8/11

# Version History
# 1. Create New                         R.Ishikawa  Ver.1.1  2020/8/11

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import subprocess

# 自動操作対象URL
target_url = "https://www.rakuten-sec.co.jp/"

# ドライバー格納先
driver_path = "WEBDRIVER PATH"

# ログインID
login_id = "YOUR LOGIN ID"

# パスワード
password = "YOUR PASSWORD"

driver = webdriver.Chrome(driver_path)
driver.get(target_url)

# ログインIDをインプットする
login_id_box = driver.find_element_by_xpath('//*[@id="form-login-id"]')
login_id_box.send_keys(login_id)

# パスワードをインプットする
password_box = driver.find_element_by_xpath('//*[@id="form-login-pass"]')
password_box.send_keys(password)

time.sleep(3)

# ログインボタンを探す
login_button = driver.find_element_by_xpath('//*[@id="VISITOR_INDEX"]/section[1]/div/div/div[3]/div[1]/form/button')


#ログインボタンをクリック
login_button.click()

time.sleep(3)
