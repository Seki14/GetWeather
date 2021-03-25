# coding: utf-8

# Tool name         :AutoLoginNISA
# Module name       :AutoLoginNISA.py
# Detail            :楽天証券のWEBページへのログインと資産一覧スクリーンショットを自動で取得するスクリプト
# Implementer       :R.Ishikawa
# Version           :1.4
# Last update       :2021/3/25

# HISTORY
#1 新規作成                                                  Ver.1.1  R.I  2020/10/19
#2 スクリーンショットを取得する処理を追加                         Ver.1.2  R.I  2020/11/22
#3 CSV取得を廃止。ヘッドレスモードで起動する処理に変更。            Ver.1.3  R.I  2020/12/5
#4 ChromedriverのVer.が古い場合に最新版をインストールする処理追加  Ver.1.4  R.I  2021/3/25

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import shutil
import datetime

# 自動操作対象URL
target_url = "https://www.rakuten-sec.co.jp/"

# スクリーンショット格納先
asset_screenshot_path = "/[任意の階層]/01_Asset/"
TotalReturn_screenshot_path = "[任意の階層]/02_ToTalReturn/"
graph_screenshot_path = "/[任意の階層]/03_Graph/"

# スクリーンショットファイルパス
asset_screenshot_file = asset_screenshot_path + "Asset" + "_" + datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + ".png"
TotalReturn_screenshot_file = TotalReturn_screenshot_path + "TotalReturn" + "_" + datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + ".png"
graph_screenshot_file = graph_screenshot_path + "Graph" + "_" + datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + ".png"

# 証券番号
login_id = "証券番号を入力"
# パスワード
password = "パスワードを入力"

# Chrome Driverをヘッドレスモードで起動する
options = Options()
options.add_argument('--headless')
# Chromedriverのバージョンが古い場合、最新版をインストールする。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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

# Chrome画面の横幅・縦幅の長さ
screenshot_wedth = driver.execute_script("return document.body.scrollWidth")
screenshot_height = driver.execute_script("return document.body.scrollHeight")
# Chrome画面の縦幅・横幅の長さを取得。
driver.set_window_size(screenshot_wedth,screenshot_height)
# スクリーンショットを取得し、ScreenShotディレクトリ直下にPNGファイルを保存。
driver.save_screenshot(asset_screenshot_file)

time.sleep(3)

# トータルリターンボタンを探す
total_return_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/div/ul/li[4]/a')
# トータルリターンボタンをクリック
total_return_button.click()

# Chrome画面の横幅・縦幅の長さ
screenshot_wedth = driver.execute_script("return document.body.scrollWidth")
screenshot_height = driver.execute_script("return document.body.scrollHeight")
# Chrome画面の縦幅・横幅の長さを取得。
driver.set_window_size(screenshot_wedth,screenshot_height)
# スクリーンショットを取得し、ScreenShotディレクトリ直下にPNGファイルを保存。
driver.save_screenshot(TotalReturn_screenshot_file)

time.sleep(3)

# 投信あしあとボタンを探す
toushin_ashiato_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/div/ul/li[7]/a')
# 投資信託ボタンをクリック
toushin_ashiato_button.click()

time.sleep(3)

# グラフ表示ボタンを探す
show_graph_button = driver.find_element_by_xpath('//*[@id="str-main-inner"]/table/tbody/tr/td/form/div[6]/table/tbody/tr/td/a/img')
# グラフ表示ボタンをクリック
show_graph_button.click()

# Chrome画面の横幅・縦幅の長さ
screenshot_wedth = driver.execute_script("return document.body.scrollWidth")
screenshot_height = driver.execute_script("return document.body.scrollHeight")
# Chrome画面の縦幅・横幅の長さを取得。
driver.set_window_size(screenshot_wedth,screenshot_height)
# スクリーンショットを取得し、ScreenShotディレクトリ直下にPNGファイルを保存。
driver.save_screenshot(graph_screenshot_file)

time.sleep(3)

driver.quit()
exit()
