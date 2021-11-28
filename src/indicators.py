"""
Dan Thayer - playing with python and indicators in pursuit of profit
Oct 2021

"""

import pandas as pd
import numpy as np
import datetime as dt


class Indicators:

    @staticmethod
    def calc_sma(df_price, lookback=14):
        """
        Calculate simple moving average of a given dataframe with target lookback number of days
        :param df_price: price Pandas dataframe
        :param lookback: number of days to average over (default 14)
        :return: Pandas dataframe of price simple moving average
        """
        return df_price.rolling(window=lookback, min_periods=lookback).mean()

    def calc_bollinger_bands(self, df_price, lookback=14):
        """
        Calculate bollinger bands of a given price dataframe, which bounds the simple moving average of the price,
        2 standard deviations above and below
        :param df_price: price Pandas dataframe
        :param lookback: number of days to average over (default 14)
        :return: [bollinger percentage from [0.0, 1.0] where 0.0 is lower band and 1.0 is top band, top band, bottom band]
        """
        rolling_std = df_price.rolling(window=lookback, min_periods=lookback).std()
        sma = self.calc_sma(df_price, lookback)
        top_band = sma + (2 * rolling_std)
        bottom_band = sma - (2 * rolling_std)
        bbp = (df_price - bottom_band) / (top_band - bottom_band)
        return bbp, top_band, bottom_band

    @staticmethod
    def calc_macd(self, df_price, lookback1=12, lookback2=26):
        """
        create moving average convergence/divergence oscillator which subtracts longer moving avg from shorter one
        :param self:
        :param df_price:
        :param lookback1: days for first moving avg (default 12)
        :param lookback2: days for second (longer) moving avg (default 26)
        :return:
        """
        ema_long = df_price.ewm(span=lookback2, adjust=False).mean()
        ema_short = df_price.ewm(span=lookback1, adjust=False).mean()
        return ema_short - ema_long