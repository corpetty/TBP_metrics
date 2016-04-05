__author__ = 'Corey Petty'
import pandas as pd

dailyFile = input("Please input the daily downloads filename: ")
daily_metrics = pd.DataFrame.from_csv(dailyFile, index_col=None, parse_dates=[0])
