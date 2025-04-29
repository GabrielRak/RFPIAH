import json
import yfinance as yf
from utils.utils import check_if_path_exists
import requests

#Stock market

def download_ticker(ticker,period="1mo"):
    """
        Downloads the ticker data from Yahoo Finance and saves it to a JSON file.
    """
    data = yf.Ticker(ticker)

    file_name = f'data/json/{ticker}'
    check_if_path_exists(f'data/json/stock/{ticker}')
    
    data.history(period=period).to_json(f"{file_name}.json", orient='index')
    
    
#Crypto 

def test_connection():
    """
        Tests the connection to the Binance API.
    """
    return requests.get("https://api.binance.com/api/v3/ping")


def get_crypto_data(symbol="BTCUSDT", limit=5, endpoint="ping"):
    """
        Gets the crypto data from Binance API.
    """
    url = "https://api.binance.com/api/v3/" + endpoint
    response = requests.get(url, params={"symbol": symbol, "limit": limit, "interval":"1d"})
    return response.json()


CRYPTO_ENDPOINTS = [
    'klines',
    'depth',
    'trades',
    'aggTrades',
]

if test_connection():
    for i in CRYPTO_ENDPOINTS:
        params = {"symbol": "BTCUSDT", "limit": 15}
        if i == "klines":
            params["interval"] = "1d"  # Add additional parameter for 'klines'

        data = requests.get(f"https://api.binance.com/api/v3/{i}", params=params).json()
        file_name = f'data/json/crypto/{params["symbol"]}/{i}'
        check_if_path_exists(f'data/json/crypto/{params["symbol"]}')
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f)
        print(f"Downloaded {i} data")
else:
    print("Connection failed")
    exit(1)

