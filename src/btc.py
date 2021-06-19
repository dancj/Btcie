# Btcie bitcoin trend notifier
# Started June 2021

import pandas as pd
import numpy as np
import ta.utils
import ta.volatility
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime


def main(data_src):
    print("analyzing", data_src, "starting at", datetime.now())

    df = pd.read_csv(data_src, sep=',')
    df = ta.utils.dropna(df)
    t = np.array(df.index)

    # bollinger bands
    bb = ta.volatility.BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_bbm'] = bb.bollinger_mavg()
    df['bb_bbh'] = bb.bollinger_hband()
    df['bb_bbl'] = bb.bollinger_lband()
    df['bb_bbpercent'] = bb.bollinger_pband()

    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])
    ax1 = plt.subplot(gs[0, 0])
    ax1.set_ylabel('Price')
    ax1.fill_between(t, df['bb_bbm'].values.flatten(), df['bb_bbh'].values.flatten(), facecolor='green', alpha=0.2)
    ax1.fill_between(t, df['bb_bbm'].values.flatten(), df['bb_bbl'].values.flatten(), facecolor='red', alpha=0.2)
    df['bb_bbm'].plot(ax=ax1)
    df['bb_bbh'].plot(ax=ax1)
    df['bb_bbl'].plot(ax=ax1)
    df["Close"].plot(ax=ax1, title="Close Price", legend=True, linestyle='dashed')

    ax2 = plt.subplot(gs[1, 0], sharex=ax1)
    df['bb_bbpercent'].plot(ax=ax2, title="BB Percent")
    ymin, ymax = ax2.get_ylim()
    ax2.set_ylabel("BBP %")
    plt.axhline(y=1, color='grey', linestyle='--', linewidth=1)
    plt.axhline(y=0, color='grey', linestyle='--', linewidth=1)
    plt.show()


if __name__ == "__main__":
    main(data_src="data/BTC-USD.csv")
