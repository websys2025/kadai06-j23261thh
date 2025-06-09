"""
東京都オープンデータAPIからデータを取得するプログラム

参照するオープンデータ:
    名前: 地下鉄関連情報 各駅乗降人員一覧
    概要: 2023年4月～2024年3月の都営地下鉄浅草線各駅の一日平均乗降人員を駅ごとに掲載したデータ
エンドポイント(URL):
    https://www.opendata.metro.tokyo.lg.jp/kotsu/subway_passengers_asakusa.csv

"""

import requests, csv, sys

url = "https://www.opendata.metro.tokyo.lg.jp/kotsu/subway_passengers_asakusa.csv"
r = requests.get(url)
r.encoding = 'cp932'
lines = r.text.splitlines()
reader = csv.DictReader(lines)
if reader.fieldnames and reader.fieldnames[0] == '':
    reader.fieldnames[0] = '駅名'
data = list(reader)
for row in data[:5]:
    print(row)
