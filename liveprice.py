import pandas as pd
import json

url = 'http://www.nepalstock.com/stocklive'

def scrapper(url):
    table = pd.read_html(url)
    liveprice = pd.DataFrame(table[0])
    liveprice = json.loads('{"items":'+ liveprice.to_json(orient='records', date_format='iso')+'}')
    liveprice = liveprice['items']
    return liveprice

liveprice = scrapper(url)