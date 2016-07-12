import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from matplotlib import style
style.use('ggplot')

web_stats = {'Day': [1,2, 3, 4, 5, 6], 'visitors': ['45', '42','52','82','32','94'], 'Bounce_Rate': ['45', '42','52','82','32','94']}

df = pd.DataFrame(web_stats)

df.set_index('Day', inplace=True)

print(df)
print(df.head())
print(df.tail(2))

print(df['visitors'])
print(df.visitors)

print(df[['visitors', 'Bounce_Rate']])
print(np.array(df[['visitors', 'Bounce_Rate']]))

print(df.visitors.tolist())

df2 = np.array(df[['visitors', 'Bounce_Rate']])
df2 = pd.DataFrame(df2)

print(df2)

