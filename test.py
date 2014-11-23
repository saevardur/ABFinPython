import ABFinPython.instrument as inst
import datetime as dt
ICEAIR = inst.Instrument('ICEAIR')
d1 = dt.date(2014,10,1)
d2 = dt.date(2014,10,27)
prices = ICEAIR.getPriceSeries(d1,d2)
print(prices)
#import pandas as pd
#import pandas.io.sql as psql
#import pypyodbc
#import pymssql
#import matplotlib.pyplot as plt
#import Quandl as q


#conn = pypyodbc.connect('DRIVER={SQL Server};SERVER=dbDeli;DATABASE=VBR;Trusted_Connection=Yes;')

#is15 = psql.read_sql('SELECT dagsetning, gengi FROM Runur WHERE FlokkurID = 16719',conn)
#iceair = psql.read_sql('SELECT dagsetning, gengi FROM Runur WHERE FlokkurID = 21360',conn)

##is15.info()

##print(runa.head(10))
##is15.plot()
##iceair.plot()

##is15 = is15.set_index('dagsetning')
##iceair = iceair.set_index('dagsetning')

#df = pd.DataFrame({'is15':is15['gengi'],'iceair':iceair['gengi']},is15['dagsetning'])

##print(df.head())

##plt.plot(is15.index,is15,iceair)

##plt.xticks(is15.index[0::3],[])

##df.plot()

##plt.show()

#iceair2 = q.get('GOOG/ICE_ICEAIR')

# Euler-Maruyama
import numpy as np
import matplotlib.pyplot as plt
import math
import random
 
tBegin=0
tEnd=2
dt=.00001
 
t = np.arange(tBegin, tEnd, dt)
N = t.size 
IC=0
theta=1
mu=1.2
sigma=0.3
 
sqrtdt = math.sqrt(dt)
y = np.zeros(N)
y[0] = IC
for i in xrange(1,N):
    y[i] = y[i-1] + dt*(theta*(mu-y[i-1])) + sigma*sqrtdt*random.gauss(0,1)
 
ax = plt.subplot(111)
ax.plot(t,y)
plt.show()
