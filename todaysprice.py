import pandas as pd
import json

url = ('http://www.nepalstock.com/main/todays_price/index/2/?startDate=&stock-symbol=&_limit=500')

def scrapper(url):
    table = pd.read_html(url, skiprows=1)
    table[0].drop(table[0].tail(4).index,inplace=True)
    todaysprice = pd.DataFrame(table[0])
    todaysprice = json.loads('{"items":'+ todaysprice.to_json(orient='records', date_format='iso')+'}')
    todaysprice = todaysprice['items']
    return todaysprice

todaysprice = scrapper(url)