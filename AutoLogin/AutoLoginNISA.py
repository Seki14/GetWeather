# coding: utf-8

# Tool name         :AutoLoginNISA
# Module name       :AutoLoginNISA.py
# Detail            :楽天証券のWEBページへのログインと資産一覧のCSVファイルを自動化したスクリプト
# Implementer       :R.Ishikawa
# Version           :1.1
# Last update       :2020/10/19

# HISTORY
#1 Create New                  Ver.1.0  R.I  2020/10/19

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import shutil
import glob

# move_CSV : 条件を満たすファイルを一括で移動するメソッド
  # from_path : 移動対象のファイルの格納先ディレクトリパス
  # to_path : 移動先のディレクトリパス

def move_CSV(to_path, from_path, recursive=True):
    for p in glob.glob(from_path, recursive=recursive):
        shutil.move(p, to_path)

# 自動操作対象URL
target_url = "https://www.rakuten-sec.co.jp/"

# ドライバー格納先
driver_path = "chromedriverが格納されているパスを入力"
# 証券番号
login_id = "証券番号を入力"
# パスワード
password = "パスワードを入力"

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

# ログインボタンをクリック
login_button.click()
time.sleep(3)

# 保有商品一覧ボタンを探す
show_list_button = driver.find_element_by_xpath('//*[@id="member-top-btn-stk-possess"]')

# 保有商品一覧ボタンをクリック
show_list_button.click()
time.sleep(3)

# CSVで保存ボタンを探す
save_csv_button = driver.find_element_by_xpath('//*[@id="printLink"]/table/tbody/tr/td[4]/div/a')

# CSVで保存ボタンをクリックし、資産一覧CSVをダウンロード
save_csv_button.click()
time.sleep(3)

# ダウンロードした'assetbalance(all)_*.csv'を資産一覧ディレクトリに移動
move_CSV('[CSV保存先ディレクトリのパス]','/Users/[ユーザ名]/Downloads/assetbalance(all)_*.csv',True)
