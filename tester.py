import os
from stocksToArray import stocksToArray
from stock import Stock
switcher = {}
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


test = stocksToArray("NYSE_20191104.txt", "AMEX_20191104", "NASDAQ_20191104.txt")
stock = test.stocks["UBER"]
print("What stock are we looking at today?")
ticker = input()
stock = test.stocks[ticker.upper()]
if stock == None:
    print("Unable to find that ticker symbol")
else:
    printMenu()
    run = "y"
    switcher = {
            1: "Today " + stock._ticker + " opened at $" + stock._open,
            2: "Today " + stock._ticker + " closed at $" + stock._close,
            3: "Today " + stock._ticker + "'s high was at $" + stock._high,
            4: "Today " + stock._ticker + "'s low was at $" + stock._low,
            5: "Today " + stock._ticker + "'s volume was " + stock._volume,
            6: "Today " + stock._ticker + " opened at $" + stock._open + 
		        "\nToday " + stock._ticker + " closed at $" + stock._close + 
		        "\nToday " + stock._ticker + "'s high was at $" + stock._high +
		        "\nToday " + stock._ticker + "'s low was at $" + stock._low + 
		        "\nToday " + stock._ticker + "'s volume was " + stock._volume
    }
    while run == "y":
        num = input()
        print(switcher.get(int(num), "Invalid"))
        print("Go again? (y/n)")
        run = input()
    print("Have a great day!")

