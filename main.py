import matplotlib.pyplot as plt
from csvdebug import *


aapl['Close'].plot(label='Apple Inc. (AAPL)', figsize=(15,8), title='Adjusted closing price')
tsla['Close'].plot(label='Tesla, Inc. (TSLA)')
fb['Close'].plot(label='Facebook, Inc. (FB)')
nflx['Close'].plot(label='Netflix, Inc. (NFLX)')

# goog['Close'].plot(label='GOOG')
# btc['Close'].plot(label='BTC-USD')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.axes() 
ax.set_facecolor("#353333")

plt.show()