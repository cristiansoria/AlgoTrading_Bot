from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time
import alpacaClient
import json
import pandas as pd 

global stocks, stocksBought
stocksBought = []
stocks = {}
# df = pd.read_csv("S&P500.csv")
# stocks = list(set(df["Tickers"].values.tolist()))
# stocks.sort()

def marketHours():
    h = time.localtime(time.time()).tm_hour,time.localtime(time.time()).tm_min
    return ((6,30) < h and h < (15,30))

def get_indicators(ticker):
    key = 'VDWEV1WBSQCQRZDF'
    ti = TechIndicators(key = key, output_format='pandas')
    ts = TimeSeries(key = key, output_format='pandas')

    # RSI
    data_rsi, meta_data_rsi = ti.get_rsi(symbol = ticker, interval='30min', time_period='14', series_type='close')
    rsi = float(data_rsi.tail(1)["RSI"].iloc[-1])

    # MACD
    data_macd, meta_data_macd = ti.get_macd(symbol=str(ticker), interval='30min', series_type='close',fastperiod='12', slowperiod='26', signalperiod='9')
    macd = float(data_macd["MACD_Hist"].head(1).iloc[-1])
    prevMacd = float(data_macd["MACD_Hist"].head(2).iloc[-1])

    # EMA
    data_ema, meta_data_ema = ti.get_ema(ticker, interval='30min', time_period=9, series_type='close')
    ema = data_ema["EMA"].tail(1).iloc[-1]

    # Stoch
    # data_stoch, meta_data_stoch = ti.get_stoch(symbol = ticker, interval='30min')
    # print(data_stoch.head(1))
    # slowD = data_stoch.head(1)['SlowD'].iloc[-1]
    # slowK = data_stoch.head(1)['SlowK'].iloc[-1]
   
    # Intraday
    data_intra, meta_data_intra = ts.get_intraday(ticker, interval='30min', outputsize='compact')
    low = data_intra.head(1)['3. low'].iloc[-1]
    prevLow = data_intra.head(2)['3. low'].iloc[-1]
    
    # print(data_intra.head(3))
    # lastLow = data_intra.head(3)['4. close'].iloc[-1]
    # volume = data_intra.head(1)['5. volume'].iloc[-1]
    # prevVol = data_intra.head(2)['5. volume'].iloc[-1]

    return ((low>ema) and (macd > float(0.05)) and (rsi < 71) and (macd-prevMacd > 0.0) and (low<float(100)) and ((low-prevLow)> 0.0) and ((low-lastLow)>0.0))

def getStocks():
    f = open("sp500.txt", "r")
    # f = open("list.txt")
    global stocks
    counter = 0
    for line in f:
        value = line.split(",")
        stocks[counter] = value[0]
        counter += 1


getStocks()
iter = 0
while(marketHours()):
    ticker = stocks[iter]
    print(ticker)
    iter+=1
    if(iter>len(stocks)-1):
        iter = 0

    try:
        ans = get_indicators(ticker)
    except:
        ans = False
        print("Error getting ", ticker)

    if(ans):
        alpacaClient.create_order(ticker, 10, "buy", "market", "day")
        print("Bought " , ticker)
        stocksBought.append(ticker)
    elif ticker in stocksBought:
            alpacaClient.create_order(ticker, 10, "sell", "market", "day")
            stocksBought.remove(ticker)
            print("Sold ", ticker)