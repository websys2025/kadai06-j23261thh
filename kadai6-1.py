import requests
from itertools import islice

# 小売物価統計調査 データを取得するための設定
# 小売物価統計調査は、消費者物価指数やその他物価に関する基礎資料を得ることを目的とした調査です。毎月、全国的規模で国民の消費生活上重要な財の小売価格、サービスの料金及び家賃を、店舗及び世帯を対象に調査しています。調査結果は、年金等の給付見直しの際の基礎資料や、公共料金の上限値を決める際の資料として、幅広く利用されています。 　調査は、物価の動向を把握するための動向編と、地域別の物価の構造を把握するための構造編で構成されています。 
APP_ID = "4aa528bb64bd1362ee3d440eb30715f80174d310"
URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
params = {
    "appId": APP_ID,
    "statsDataId": "0003421913",
    "metaGetFlg": "Y",
    "cntGetFlg": "N",
    "explanationGetFlg": "Y",
    "annotationGetFlg": "Y",
    "sectionHeaderFlg": "1",
    "replaceSpChars": "0",
    "lang": "J"
}

response = requests.get(URL, params=params).json()
data = response["GET_STATS_DATA"]["STATISTICAL_DATA"]

cat02_map = {
    c["@code"]: c["@name"]
    for obj in data["CLASS_INF"]["CLASS_OBJ"] if obj["@id"] == "cat02"
    for c in (obj["CLASS"] if isinstance(obj["CLASS"], list) else [obj["CLASS"]])
}

print("年月\t都市コード\t銘柄\t価格(円)")
values = (
    v for v in data["DATA_INF"]["VALUE"]
    if v["@cat02"] == "01021"
)
for v in islice(values, 50):
    print(f'{v["@time"]}\t{v["@area"]}\t{cat02_map[v["@cat02"]]}\t{v["$"]}')

# コード1021(食パン)の価格を50件分出力