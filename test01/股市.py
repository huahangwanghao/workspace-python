import matplotlib
import  pandas as pd
import pandas_datareader.data as web
import  datetime

from matplotlib import pylab
from pip._vendor.html5lib.treeadapters.sax import namespace

start = datetime.datetime(2017,10,1)
end = datetime.date.today()
apple = web.DataReader("AAPL", "yahoo", start=start,end=end)
print(apple.head())

# goog=web.DataReader('GOOG',data_source='yahoo',start=start,end=end)
# head=goog.head()
# tail=goog.tail()
# print(head)
# print(tail)



pylab.rcParams['figure.figsize'] = (15, 9)  # Change the size of plots

apple["Adj Close"].plot(grid=True)  # Plot the adjusted closing price of AAPL



