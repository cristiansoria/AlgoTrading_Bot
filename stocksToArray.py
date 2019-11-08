from stock import Stock
class stocksToArray:
    lines = []
    stocks = {}
    counter = 0

    def __init__(self, NYSE, NASDAQ, AMEX):
        stocksToArray.scan(NYSE)
        stocksToArray.scan(NASDAQ)
        stocksToArray.scan(AMEX)
        
    def scan(fileName):
        name = fileName
        FILE = open("NYSE_20191104.txt", "r")
        for line in FILE:
            values = line.split(",")
            ticker = values[0]
            date = values[1]
            op = values[2]
            high = values[3]
            low = values[4]
            close = values[5]
            vol = values[6]
            stock = Stock(ticker, date, op, high, low, close, vol)
            stocksToArray.stocks[ticker] = stock
        FILE.close()

