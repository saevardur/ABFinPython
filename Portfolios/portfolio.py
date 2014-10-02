#!/usr/bin/env python

import instrument as inst

"""Portfolio.py: Arion bank asset holding portfolio."""

__author__      = "Saevardur Einarsson"
__copyright__   = "Copyright 2014, Arion Bank"

class Portfolio:
    """Portfolio class

    Attributes:
        portfolioID: The ID of the portfolio as defined in VBR (safnID).
        assets: A list of Holding instances which hold an asset and the nominal value contained in the portfolio.
    """
    portfolioID = null
    weightsPortfolio = false
    assets = null

	def __init__(self):
		'Init null portfolio'

	def __init__(self,pID):
		'Init empty portfolio'

		self.portfolioID = pID

	def addAsset(flokkurID,nominal):
		'Add a single asset to the portfolio'
        if (nominal < 1):
            # If nominal is less we assume it refers to the percentage weight.
            self.weightsPortfolio = true
            self.assets.append(Holding(flokkurID,nominal))

	def addAssets(assets):
		'Add a list of assets to the portfolio'

    def calculateMarketValue(date):
		'Calculate portfolio market value on a date. Default date is today'

    def calculateReturns(date):
        'Calculate portfolio returns on a date. Default date is today'

class Holding:
    """Portfolio Holding class

    Attributes
        asset: A instance of the instrument class.
        nominal: The nominal amount of the asset (can also be a weight if it is less than 1).
        buyYield: The yield at which the asset was bought.
    """
    asset = null
    nominal = null
    buyYield = null

    def __init__(self):
		'Init null holding'

	def __init__(self,flokkurID,nominal=0):
		'Init holding with instrument'
        self.asset = inst.Instrument(flokkurID)
        self.nominal = nominal

    def calculateMarketValue(date):
        'Calculate market value of holding on date. (Only works if working with nominal amount)'
        return nominal * self.asset.getClosingPrice(date)

    def calculateReturns(date):
        'Calculate holding returns on a date. Default date is today'
        # get straight from instrument
