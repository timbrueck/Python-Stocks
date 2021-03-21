import pandas_datareader as pdr
import datetime 
import pandas as pd

AAPL = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

TSLA = pdr.get_data_yahoo('TSLA',
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

GOOG = pdr.get_data_yahoo('GOOG',
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

BTC = pdr.get_data_yahoo('BTC-USD',
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

FB = pdr.get_data_yahoo('FB',
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

NFLX = pdr.get_data_yahoo('NFLX',
                          start=datetime.datetime(2016, 1, 1), 
                          end=datetime.datetime(2020, 12, 31))

# Converting data to csv-files
AAPL.to_csv('aapl.csv')
TSLA.to_csv('tsla.csv')
GOOG.to_csv('goog.csv')
FB.to_csv('fb.csv')
NFLX.to_csv('nflx.csv')



# Reading the files
aapl = pd.read_csv('aapl.csv')
tsla = pd.read_csv('tsla.csv')
goog = pd.read_csv('goog.csv')
btc = pd.read_csv('btc.csv')
fb = pd.read_csv('fb.csv')
nflx = pd.read_csv('nflx.csv')


# Converting 'Date' to the right format
aapl['Date'] = pd.to_datetime(aapl['Date'])
tsla['Date'] = pd.to_datetime(tsla['Date'])
goog['Date'] = pd.to_datetime(goog['Date'])
btc['Date'] = pd.to_datetime(btc['Date'])
fb['Date'] = pd.to_datetime(fb['Date'])
nflx['Date'] = pd.to_datetime(nflx['Date'])


aapl.head(2)
tsla.head(2)
goog.head(2)
btc.head(2)
fb.head(2)
nflx.head(2)

aapl.index = aapl['Date']
tsla.index = tsla['Date']
goog.index = goog['Date']
btc.index = btc['Date']
fb.index = fb['Date']
nflx.index = nflx['Date']