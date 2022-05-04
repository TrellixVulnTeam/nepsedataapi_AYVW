import pandas as pd
import json


url = 'http://www.nepalstock.com/main/floorsheet/index/2/?contract-no=&stock-symbol=&buyer=&seller=&_limit=50000'

def scrapper(url):
    table = pd.read_html(url, skiprows=1)
    table = table[0].drop(table[0].tail(3).index)
    floorsheet = pd.DataFrame(table)
    floorsheet.dropna(axis=1,inplace = True)
    floorsheet = json.loads('{"items":'+ floorsheet.to_json(orient='records', date_format='iso')+'}')
    floorsheet = floorsheet['items']
    return floorsheet

floorsheet = scrapper(url)
print(floorsheet)