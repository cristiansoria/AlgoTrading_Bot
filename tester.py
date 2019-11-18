import os
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from stocksToArray import stocksToArray
from stock import Stock
from pprint import pprint

apiKey = "QFCCLPPV74UFP4OK"
belowRSI = {}


def printMenu():
	print("          Menu          ")
	print("------------------------")
	print("1) Opening Price")
	print("2) Closing Price")
	print("3) HOD (High of the Day)")
	print( "4) LOD (Low of the Day)")
	print("5) Volume")
	print("6) All of the Above")
	print("------------------------")  
def print6(ticker, num):
    if int(num) == 1 :
        ts = TimeSeries(key=apiKey,output_format='pandas', indexing_type='date')
        data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
        print(data.head(6))
    if int(num) == 2 :
        ts = TimeSeries(key=apiKey,output_format='pandas', indexing_type='close')
        print(ts)
    if int(num) == 3 :
        ts = TimeSeries(key=apiKey,output_format='pandas', indexing_type='high')
        print(ts)
    if int(num) == 4 :
        ts = TimeSeries(key=apiKey,output_format='pandas', indexing_type='low')
        print(ts)
    if int(num) == 5 :
        ts = TimeSeries(key=apiKey,output_format='pandas', indexing_type='volume')
        print(ts)
    if int(num) == 6 :
        ts = TimeSeries(key=apiKey, output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
        pprint(data.head(2))

run = "y"
test = stocksToArray("NYSE_20191104.txt", "AMEX_20191104", "NASDAQ_20191104.txt")
print(test.size())
print(test.printRSI())

# while run == "y":
#     print("What stock are we looking at today?")
#     ticker = input()

#     printMenu()
#     num = input()
#     print6(ticker, num)
#     print("Go again? (y/n)")
#     run = input()
# print("Have a great day!")

