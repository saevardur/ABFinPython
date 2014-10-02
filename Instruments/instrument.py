#!/usr/bin/env python

import dataaccess as da
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
    flokkurID = null
    audkenni = null
    prices = null
    yields = null # bond class?
    cleanPrices = null # bond class?


    def __init__(self):
        'Init null instument'

    def __init__(self,flokkurID):
        'Init instrument with flokkurID'
        self.flokkurID = flokkurID
        self.audkenni = da.getAudkenni(flokkurID)

    def __init__(self,audkenni):
        'Init instrument with audkenni'
        self.audkenni = audkenni
        self.flokkurID = da.getFlokkurID(audkenni)

    def getClosingPrice(date):
        'Get closing price for date from Vog. Default last business day.'

    def getClosingYield(date):
        'Get closing yield for date from Vog. Default last business day. Only works for bonds, should maybe be another class.'

    def calculateReturns(date):
        'Calculate returns. Should probably take in date range, where the default for starting date is the first date and ending date is last business day.'

    def calculateLogReturns(date):
        'Calculate log returns. Should probably take in date range, where the default for starting date is the first date and ending date is last business day.'

    def plotPrice():
        'Plot price'

    def plotReturns():
        'Plot returns'

    def plotLogReturns():
        'Plot returns'
