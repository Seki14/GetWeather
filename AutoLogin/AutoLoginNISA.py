# coding: utf-8

# Tool name         :AutoLoginNISA
# Module name       :AutoLoginNISA.py
# Detail            :楽天証券のWEBページへのログインと資産一覧のCSVファイルを自動化したスクリプト
# Implementer       :R.Ishikawa
# Version           :1.2
# Last update       :2020/10/22

# HISTORY
#1 新規作成                            Ver.1.1  R.I  2020/10/19
#2 スクリーンショットを取得する処理を追加     Ver.1.2  R.I  2020/11/22

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import shutil
import glob
import datetime

# move_CSV : 条件を満たすファイルを一括で移動するメソッド
  # from_path : 移動対象のファイルの格納先ディレクトリパス
  # to_path : 移動先のディレクトリパス

def move_CSV(to_path, from_path, recursive=True):
    for p in glob.glob(from_path, recursive=recursive):
        shutil.move(p, to_path)

# 自動操作対象URL
target_url = "https://www.rakuten-sec.co.jp/"

# 資産一覧CSV格納先
csv_path = "[資産一覧CSVファイルを格納したいディレクトリパス]"
# スクリーンショット格納先
screenshot_path = "[スクリーンショットを格納したいディレクトリパス]"
# スクリーンショットファイルパス
screenshot_file = screenshot_path + datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + ".png"

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

# ダウンロードした資産一覧CSVを資産一覧ディレクトリに移動
move_CSV(csv_path,'/Users/[ユーザ名]/Downloads/assetbalance(all)_*.csv',True)

# Chrome画面の横幅・縦幅の長さ
screenshot_wedth = driver.execute_script("return document.body.scrollWidth")
screenshot_height = driver.execute_script("return document.body.scrollHeight")

# Chrome画面の縦幅・横幅の長さを取得。
driver.set_window_size(screenshot_wedth,screenshot_height)

# スクリーンショットを取得し、imageディレクトリ直下にPNGファイルを保存。
driver.save_screenshot(screenshot_file)
