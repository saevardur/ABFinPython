import pandas as pd
import pandas.io.sql as psql
import pymssql

def getAudkenni(flokkurID):
    'Get audkenni from flokkurID'
    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.cursor()
    query = 'SELECT audkenni FROM Flokkur WHERE FlokkurID = ' + flokkurID
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()


def getFlokkurID(audkenni):
    'Get flokkurID from audkenni'
    conn = pymssql.connect(host='dbDeli',database='VBR')
    cur = conn.curser()
    query = "SELECT flokkurID FROM Flokkur WHERE audkenni = '" + audkenni + "'"
    cur.execute(query)

    for row in cur:
        return row[0]

    conn.close()
