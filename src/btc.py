# Btcie bitcoin trend notifier
# Started June 2021

import pandas as pd
import numpy as np
import yfinance as yf
import ta.utils
import ta.volatility
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime


CONFIG_LOCAL_DATA = False


def fetch_data(symbol):
    # local datafile
    if CONFIG_LOCAL_DATA:
        path = "data/{0}.csv".format(symbol)
        data = pd.read_csv(path, sep=',')
    else:
        # fetch from yahoo finance
        data = yf.download(tickers=symbol, period='300d', interval='1d')
    return data


def main(symbol):
    print("analyzing", symbol, "starting at", datetime.now())

    df = fetch_data(symbol  )
    df = ta.utils.dropna(df)
    t = np.array(df.index)

    # bollinger bands
    bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_MovingAvg'] = bb.bollinger_mavg()
    df['bb_bbh'] = bb.bollinger_hband()
    df['bb_bbl'] = bb.bollinger_lband()
    df['bb_bbpercent'] = bb.bollinger_pband()

    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])
    ax1 = plt.subplot(gs[0, 0])
    ax1.set_ylabel('Price')
    ax1.fill_between(t, df['bb_MovingAvg'].values.flatten(), df['bb_bbh'].values.flatten(), facecolor='green', alpha=0.2)
    ax1.fill_between(t, df['bb_MovingAvg'].values.flatten(), df['bb_bbl'].values.flatten(), facecolor='red', alpha=0.2)
    df['bb_MovingAvg'].plot(ax=ax1, legend=True)
    df['bb_bbh'].plot(ax=ax1)
    df['bb_bbl'].plot(ax=ax1)
    df["Close"].plot(ax=ax1, legend=True, linestyle='dashed', title=symbol)

    ax2 = plt.subplot(gs[1, 0], sharex=ax1)
    df['bb_bbpercent'].plot(ax=ax2)
    ax2.set_ylabel("BBP %")
    ax2.set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.axhline(y=1, color='grey', linestyle='--', linewidth=1)
    plt.axhline(y=0, color='grey', linestyle='--', linewidth=1)
    plt.savefig("out/bollinger_" + symbol + ".png")
    plt.show()


if __name__ == "__main__":
    main(symbol="BTC-USD")
    main(symbol="ETH-USD")
