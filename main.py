from fastapi import FastAPI
import todaysprice as tps
import liveprice as lps
import floorsheet as fls
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Welcome To Nepse Live Data API'}

@app.get('/liveprice')
async def liveprice():
    return lps.liveprice

@app.get('/todayprice')
async def todaysprice():
    return tps.todaysprice

@app.get('/floorsheet')
async def floorsheet():
    return fls.floorsheet