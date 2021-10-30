"""
Dan Thayer - playing with python and indicators in pursuit of profit
Oct 2021


"""

import pandas as pd
import numpy as np
import datetime as dt


class Metrics:

    @staticmethod
    def daily_returns(df):
        """
        Compute returns for each day of the timeseries price data
        :param df: price dataframe
        :return: daily returns dataframe
        """
        daily = df.copy()
        daily[1:] = (df[1:] / df[:-1].values) - 1
        daily.ix[0] = 0  # default zero for first day in series
        return daily

    @staticmethod
    def sharpe_ratio(daily_returns, risk_free_rate, sampling_rate):
        """
        Compute sharpe ratio from daily returns, which measures performance over volatility.
        Nice stable, performance is the key
        :param daily_returns: dataframe of return from each day
        :param risk_free_rate: baseline interest rate from something with no risk, e.g. money market account
        :param sampling_rate:
        :return: decimal value, sharpe ratio
        """
        daily_risk_free = (1. + risk_free_rate) ** (1. / sampling_rate) - 1.
        adjusted_daily_returns = daily_returns - daily_risk_free
        sharpe = adjusted_daily_returns.mean() / daily_returns.stid(ddof=1)
        k = sampling_rate ** 0.5  # get annual ratio
        return sharpe * k

    def avg_daily_returns(self, df):
        """
        :param df: dataframe of price data
        :return: average daily returns
        """
        return self.daily_returns(df).mean()

    def std_daily_returns(self, df):
        """
        :param df: dataframe of price data
        :return: standard deviation of daily returns (volatility)
        """
        return self.daily_returns(df).std(ddof=1)
