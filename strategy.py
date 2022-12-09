import pandas as pd
import ta


data = pd.read_csv('asset_data.csv')

data = ta.utils.dropna(data)
macd = ta.trend.macd(data, n_fast=12, n_slow=26)

if macd > signal:
    # generate a buy signal
elif macd < signal:
    # generate a sell signal

if signal == 'buy':
    bot.buy(asset, quantity, price)
elif signal == 'sell':
    bot.sell(asset, quantity, price)
