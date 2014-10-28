import pandas as pd
import pandas.io.sql as psql
import pymssql
import datetime as dt
from dateutil.relativedelta import relativedelta

import Quandl as q

def getLibraAudkenni(flokkurID):
    'Get audkenni from flokkurID'
    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = 'SELECT audkenni FROM Flokkur WHERE FlokkurID = ' + flokkurID
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()


def getLibraFlokkurID(audkenni):
    'Get flokkurID from audkenni'
    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = "SELECT flokkurID FROM Flokkur WHERE audkenni = '" + audkenni + "'"
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()

def getLibraClosingPriceDirty(flokkurID, date):
    'Get closing dirty price for instrument with flokkurID on date'
    if date == None:
        date = dt.date.today()

    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = "SELECT fnFlokkurGengiScalar('" + str(date) + "', " + str(flokkurID) + ", 1)"
    #query = "SELECT Gengi FROM Runur WHERE flokkurId = " + str(flokkurID) + " and dagsetning = '" + str(date) + "'"
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()

def getLibraClosingPriceClean(flokkurID, date):
    'Get closing clean price for instrument with flokkurID on date'
    if date == None:
        date = dt.date.today()

    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = "SELECT fnFlokkurGengiScalar('" + str(date) + "', " + str(flokkurID) + ", 0)"
    #query = "SELECT Gildi2 FROM Runur WHERE flokkurId = " + flokkurID + " and dagsetning = '" + date + "'" # format date
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()

def getLibraClosingYield(flokkurID, date):
    'Get closing yield for instrument with flokkurID on date'
    if date == None:
        date = dt.date.today()

    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = "SELECT Gildi1 FROM Runur WHERE flokkurId = " + str(flokkurID) + " and dagsetning = (SELECT MAX(dagsetning) FROM Runur WHERE flokkurId = " + str(flokkurID) + " AND dagsetnging < DATEADD(DAY,1,'" + str(date) + "'))"
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()

def getLibraPriceSeries(flokkurID, dateFrom, dateTo):
    'Get price series'
    if dateTo == None:
        dateTo = dt.date.today()

    if dateFrom == None:
        dateFrom = dt.date(year = 1900)

    # want only one value for each day!

    conn = pymssql.connect(host='dbDeli',database='VBR')
    return psql.read_sql("SELECT dagsetning, gengi FROM Runur WHERE FlokkurID = " + str(flokkurID) + " AND dagsetning between '" + str(dateFrom) + "' AND (SELECT MAX(dagsetning) FROM Runur WHERE flokkurId = " + str(flokkurID) + " AND dagsetning < DATEADD(DAY,1,'" + str(dateTo) + "'))",conn)

def getQuandlPriceSeries(ticker, dateFrom, dateTo):
    return q.get('GOOG/ICE_ICEAIR')