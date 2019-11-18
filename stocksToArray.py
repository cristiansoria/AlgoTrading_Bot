from stock import Stock
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from stock import Stock
from pprint import pprint
import time

class stocksToArray:
    lines = []
    stocks = {}
    global counter
    counter = 0
    global keys
    keys = ["ZPOID64EYY2JMOC5","U0V10X8KWT3Y0368","CRFTUROK1HPVS55O","18BITBBQR31LHRW7","KTIN9M8QS0I7W13K","ZYETHSY60KTQ4N7H","US8ADXJLSBQN04FS","89DJ6H1OO71V5N3C","QFCCLPPV74UFP4OK", "JT2GD5DAUZ4NY3WJ", "4V0ZD7A7O9VTMQFU", "IX340DRBYAC8LMGN","DXB27ULGE9PUTHTX", "GMFBG6KDOKBZXBEJ","D43E64SGF373HBGZ"
    ,"FMRRF5OG0O4ECTND", "NVC2MMA2OGI9H7BO","EDEF1XN0KDCVE9AM","FA1LUXJV74ZSMSV6","R861JWXKFZWT71PP","YRLISOE796QQN5B7","2OT7IV8Z6ORPQRR5","CLLFM8MOOQPH2LFQ","2FH4YYJ86GKLX9C2","57OKB60I3475QGZN"]
    def __init__(self, NYSE, NASDAQ, AMEX):
        stocksToArray.scan(NYSE)
        # stocksToArray.scan(NASDAQ)
        # stocksToArray.scan(AMEX)
        
        
    def scan(fileName):
        name = fileName
        FILE = open("NYSE_20191104.txt", "r")
        global counter
        for line in FILE:
            values = line.split(",")
            if(stocksToArray.check(values[0])): 
                    ticker = values[0]
                    date = values[1]
                    op = values[2]
                    high = values[3]
                    low = values[4]
                    close = values[5]
                    vol = values[6]
                    stock = Stock(ticker, date, op, high, low, close, vol)
                    stocksToArray.stocks[counter] = stock
                    counter+=1
        FILE.close()

    def size(self):
        return counter

    def printRSI(self):
        num = 0
        global keys
        print(keys[num])
        idk = 4
        file1 = open("RSI.txt", "a")
        for i in range(counter):
            time.sleep(13)
            if(idk == 4):
                    idk = 0
                    num += 1
                    key = keys[num]
                    if(num == 24):
                        num = 0
            this_stock = stocksToArray.stocks[i+1]
            ticker = this_stock._ticker
            if("." not in str(ticker)):
                print(ticker)
                ti = TechIndicators(key=key, output_format='pandas')
                try:
                    data, meta_data = ti.get_rsi(symbol=str(ticker), interval='daily', time_period=14, series_type='close')
                    print(data.tail(1))
                    string = str(data.tail(1))

                    for number in string.split():
                        rsi = number
                    
                    try:
                        if (float(rsi) < float(30)):
                            print(ticker + " RSI is less that 30 = " + rsi)
                            file1.write(ticker + " RSI is less that 30 = " + rsi + "\n")
                    except:
                        print("unable to get " + ticker + data)
                except:
                    print("No Value")
                idk +=1
        file1.close()

    def check(tik):
        for element in range(0, len(tik)): 
            if(tik[element] == "." or tik[element] == "-"):
                     return False
            else:
                answer = True
        return answer