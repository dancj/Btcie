"""
Dan Thayer - playing with python and indicators in pursuit of profit
Oct 2021
"""

import pandas as pd
import os
from ta.others import daily_return
from ta.utils import dropna
import plots
import matplotlib.pyplot as plt


def runner(path):
    print("reading data from: ", path)
    df = pd.read_csv(path)
    df = dropna(df)
    daily_ret = daily_return(df["Close"])
    print(daily_ret.tail())
    df.plot(x="Date", y="Close", title="BTC Closing Price")
    plt.show()
    

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "../lib/BTC-USD.csv")
    runner(path)
