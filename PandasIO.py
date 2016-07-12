import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('Data/MedianHomePrices06062.csv')
df.set_index('Date', inplace=True)
print(df.head())

df.to_csv('Data/NewCSV.csv')
df2 = pd.read_csv('Data/NewCSV.csv', index_col=0)
df2.columns = ['Plainville_HPI']
print(df2.head())

df.to_html('Data/example.html')
