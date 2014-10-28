#!/usr/bin/env python

import ABFinPython.dataaccess as da
import pandas as pd

"""Instrument.py: Basic instrument class."""

__author__      = "Saevardur Einarsson"
__copyright__   = "Copyright 2014, Arion Bank"

class Instrument:
    """Instrument
  
    Attributes:
        flokkurID:
        audkenni:
    """

    flokkurID = None
    audkenni = None
    prices = None
    yields = None # bond class?
    cleanPrices = None # bond class?
  

    def __init__(self):
        'Init null instrument'

    def __init__(self,flokkurID):
        'Init instrument with flokkurID'

        self.flokkurID = flokkurID
        self.audkenni = da.getLibraAudkenni(flokkurID)

    def __init__(self,audkenni):
        'Init instrument with audkenni'

        self.audkenni = audkenni
        self.flokkurID = da.getLibraFlokkurID(audkenni)

    def getClosingPrice(self, date=None, clean=False):
        'Get closing price for date from Vog. Default dirty price. Default last business day.'

        if (clean):
            return da.getLibraClosingPriceClean(self.flokkurID, date)
        else:
            return da.getLibraClosingPriceDirty(self.flokkurID, date)

    def getClosingYield(self, date=None):
        'Get closing yield for date from Vog. Default last business day. Only works for bonds, should maybe be another class.'

        return da.getLibraClosingYield(self.flokkurID, date)

    def getPriceSeries(self, dateFrom=None,dateTo=None):
        'DataFrame with price series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        return da.getLibraPriceSeries(self.flokkurID, dateFrom, dateTo)

    def getReturnSeries(self, dateFrom=None,dateTo=None):
        'DataFrame wiht returns series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        price = getPriceSeries(dateFrom,dateTo)
        return price.pct_change

    def getLogReturnsSeries(self, dateFrom=None,dateTo=None):
        'DataFrame with log returns series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        price = getPriceSeries(dateFrom,dateTo)
        return log(price.pct_change)

        #returns = (vfiax_monthly.open - vfiax_monthly.open.shift(1))/vfiax_monthly.open
        #returns    = log(adj_close/adj_close.shift(1))   

        #calc_returns = lambda x: np.log(x / x.shift(1))[1:]
        #returns = prices.apply(calc_returns)


    def plotPrice(self, dateFrom=None,dateTo=None):
        'Plot price series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        dataFrame = self.getPriceSeries(self, dateFrom, dateTo)

    def plotReturns(self, dateFrom=None,dateTo=None):
        'Plot return series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        dataFrame = self.getReturnSeries(self, dateFrom, dateTo)

    def plotLogReturns(self, dateFrom=None,dateTo=None):
        'Plot log return series. The default for starting date is the first date and ending date is last business day. First and last date are included in the series.'

        dataFrame = self.getLogReturnsSeries(self, dateFrom, dateTo)
