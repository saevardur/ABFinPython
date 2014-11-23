import ABFinPython.portfolio as port
import datetime as dt

d1 = dt.date(2014,10,1)
d2 = dt.date(2014,10,27)

basePortfolio = port.Portfolio()
basePortfolio.addAsset(13243,0.1) #MXWO
basePortfolio.addAsset(11550,0.20) #OMXI15
basePortfolio.addAsset(1109,0.05) #USD
basePortfolio.addAsset(18077,0.35) #HFF150224
basePortfolio.addAsset(18079,0.30) #HFF150434
