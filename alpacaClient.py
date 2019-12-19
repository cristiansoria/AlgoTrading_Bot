import requests, json
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
ACC_URL = "{}/v2/account".format(BASE_URL)
ORDER_URL = "{}/v2/orders".format(BASE_URL)
GET_POSITION = "{}//v2/positions/".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID':'PK1RHT54A1MJ70ZKDNS6', 'APCA-API-SECRET-KEY': 'T7nSaAnr6xpdnW4EvgkfmVrx3Hgz6feZCjqQnU7v'}
def get_account():
    r = requests.get(ACC_URL, headers= HEADERS)
    print(json.loads(r.content))

def create_order(symbol, qty, side, type1, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type1,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDER_URL, json = data, headers = HEADERS)
    return json.loads(r.content)



# get_account()
# response = create_order("UGAZ", 1000, "buy", "market", "gtc")
# print(response)
# parsed_json =get_position("UGAZ", "UGAZ")
# qty = parsed_json['qty:']
# print(qty)