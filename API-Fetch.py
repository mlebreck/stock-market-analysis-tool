import requests
import pandas as pd
import time

API_KEY = 'Z8UD0DRARMX0BGQV'
SYMBOLS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.B', 'V', 'JNJ', 'WMT']
BASE_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}'

for symbol in SYMBOLS:
    response = requests.get(BASE_URL.format(symbol=symbol, apikey=API_KEY))
    data = response.json()
    
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        df.to_csv(f'stock_data_{symbol}.csv')
        print(f"Data for {symbol} saved to stock_data_{symbol}.csv")
    else:
        print(f"Failed to fetch data for {symbol}. Response: {data}")
    
    # Sleep to respect API rate limits
    time.sleep(12)  # 5 calls per minute allowed by Alpha Vantage
