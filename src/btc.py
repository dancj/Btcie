# Btcie bitcoin trend notifier
# Started June 2021

import pandas as pd
import ta.utils
import ta.volatility
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime


def main(data_src):
    print("analyzing", data_src, "starting at", datetime.now())

    df = pd.read_csv(data_src, sep=',')
    df = ta.utils.dropna(df)

    # bollinger bands
    bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_bbm'] = bb.bollinger_mavg()
    df['bb_bbh'] = bb.bollinger_hband()
    df['bb_bbl'] = bb.bollinger_lband()

    gs = gridspec.GridSpec(1, 1, height_ratios=[1])
    ax1 = plt.subplot(gs[0, 0])
    ax1.set_ylabel('Price')
    df['bb_bbm'].plot(ax=ax1)
    df['bb_bbh'].plot(ax=ax1)
    df['bb_bbl'].plot(ax=ax1)
    df["Close"].plot(ax=ax1, title="Close Price")
    plt.show()


if __name__ == "__main__":
    main(data_src="data/BTC-USD.csv")
