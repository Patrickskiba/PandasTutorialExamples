import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 7, 10)

df = web.DataReader("AAPL", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
