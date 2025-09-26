import sqlite3
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import json

# primeramente creamos una funcion que conecte con la API solicitada, read(). decode(), y un return con json.loads

sqlconect = sqlite3.connect('database.sqlite')
conn = sqlconect.cursor()

conn.executescript('''
DROP TABLE IF EXISTS Realstate_Jobs;             

CREATE TABLE IF NOT EXISTS Realstate_Jobs
    (id INTEGER PRIMARY KEY AUTOINCREMENT, Year INTEGER, Industry_Jobs INTEGER, Source TEXT
    );
''')


def get_api(urlvar):
    try:
        connect = urllib.request.urlopen(urlvar)   
        data = connect.read().decode()
        return json.loads(data.strip())    

    except Exception as e:
        print("error para conectarse con API")

# conexion de la API 1 


url = "https://honolulu-api.datausa.io/tesseract/data.jsonrecords?cube=bls_growth_industry&drilldowns=Year&measures=Industry%20Jobs"

js = get_api(url)
print (json.dumps(js, indent=4)) 

for itevar in js["data"]:
    print(itevar["Year"])
    print(itevar["Industry Jobs"])
    Year = itevar["Year"]
    Industry =  itevar["Industry Jobs"]

    conn.execute('''INSERT OR IGNORE INTO Realstate_Jobs (Year, Industry_Jobs, Source)
    VALUES ( ?, ?, ?)''', (Year, int(Industry), 'National'))
    sqlconect.commit()

# conexion de la API 2 

url = "https://honolulu-api.datausa.io/tesseract/data.jsonrecords?cube=bls_growth_industry&Industry=531&drilldowns=Year,Industry&measures=Industry%20Jobs"

js = get_api(url)

print (json.dumps(js, indent=4)) 

for itevar in js["data"]:
    print(itevar["Year"])
    print(itevar["Industry Jobs"])
    Year = itevar["Year"]
    Industry =  itevar["Industry Jobs"]

    conn.execute('''INSERT OR IGNORE INTO Realstate_Jobs (Year, Industry_Jobs, Source)
    VALUES ( ?, ?, ?)''', (Year, Industry, 'Real State'))
    sqlconect.commit()
sqlconect.close()


