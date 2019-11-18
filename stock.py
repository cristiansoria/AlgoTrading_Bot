class Stock:
    def __init__(self, ticker, date, op, high, low, close, volume):
        self._ticker = ticker
        self._date = date
        self._open = op
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume
    
