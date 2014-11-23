#!/usr/bin/env python

import ABFinPython.instrument as inst
import ABFinPython.dataaccess as da
import pandas as pd
import datetime as dt

"""Portfolio.py: Arion bank asset holding portfolio."""

__author__      = "Saevardur Einarsson"
__copyright__   = "Copyright 2014, Arion Bank"

class Portfolio:
    """Portfolio class
    
    Attributes:
        portfolioID: The ID of the portfolio as defined in VBR (safnID).
        assets: A list of Holding instances which hold an asset and the nominal value contained in the portfolio.
    """
    portfolioID = 0
    weightsPortfolio = False
    assets = []

    def __init__(self,pID=0):
        'Init portfolio with portfolioID'

        if (pID > 0):
            self.portfolioID = pID
            self.instantiatePortfolioFromPortfolioID()

    def instantiatePortfolioFromPortfolioID(self):
        'Create a portfolio using the portfolioID. Get assets and nominal amount from PortfolioHoldings database. Default date is today (end of yesterday).'

        #self.assets = da.getPortfolioHoldings(self.portfolioID,dt.date.today())
        holdings = da.getPortfolioHoldings(self.portfolioID,dt.date.today())

        for row in holdings:
            self.addAsset(row[0],row[1])

    def addAsset(self,flokkurID,nominal):
        'Add a single asset to the portfolio'
        if (nominal < 1.0):
            # If nominal is less we assume it refers to the percentage weight.
            self.weightsPortfolio = True

        self.assets.append(Holding(flokkurID,nominal))

    def addAssets(self,assets):
        'Add a list of assets to the portfolio'

    def calculateMarketValue(self,date):
        'Calculate portfolio market value on a date. Default date is today (end of yesterday).'

    def calculateReturns(self,dateFrom,dateTo):
        'Calculate portfolio returnse. Default to date is today (end of yesterday), default from date is the first day of the portfolio.'

    def simulatePortfolio(self):
        'Simulate portfolio value into the future.'

class Holding:
    """Portfolio Holding class
    
    Attributes
        asset: A instance of the instrument class.
        nominal: The nominal amount of the asset (can also be a weight if it is less than 1).
        buyYield: The yield at which the asset was bought.
    """
    asset = None
    nominal = 0
    buyYield = 0

    def __init__(self):
        'Init null holding'

    def __init__(self,flokkurID,nominal=0):
        'Init holding with instrument'
        self.asset = inst.Instrument(flokkurID)
        self.nominal = nominal

    def calculateMarketValue(self,date):
        'Calculate market value of holding on date. (Only works if working with nominal amount)'
        return nominal * self.asset.getClosingPrice(date)

    def calculateReturns(self,date):
        'Calculate holding returns on a date. Default date is today'
        # get straight from instrument