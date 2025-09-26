import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Arrancamos con la conexion al API de USAgob

conn = sqlite3.connect('Construction-Related_Incidents.sqlite')
cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS Incidents_type;
DROP TABLE IF EXISTS Ubication;
DROP TABLE IF EXISTS Construction_Incidents;    

CREATE TABLE Incidents_type (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);          

CREATE TABLE Ubication (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);                  
                  
CREATE TABLE Construction_Incidents (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    date    TEXT,
    type_id    INTEGER,                  
    Fatality    TEXT,
    Injury    TEXT,
    Ubication_id    INTEGER,
    Latitude    REAL,
    Longitude    REAL                                    
);  
                                
''')

url = input('url: ')


if len(url) < 1 :
    url = 'https://data.cityofnewyork.us/api/views/bf97-mjsy/rows.json?accessType=DOWNLOAD'


document = urllib.request.urlopen(url, None, 30, context=ctx)
text = document.read().decode()

info = json.loads(text)

iter = info["data"]


for itevar in iter:
    print(itevar[10][:10])
    print(itevar[12])
    print(itevar[13])
    print(itevar[14])
    print(itevar[17])
    print(itevar[21])
    print(itevar[22])
    print('==========================================')
    print('                                          ')

    inci_date = itevar[10][:10]
    inci_type = itevar[12]
    fatality = itevar[13]
    injury = itevar[14]
    Ubication = itevar[17]
    latitude = itevar[21]
    longitude = itevar[22]

    cur.execute('''INSERT OR IGNORE INTO Incidents_type (name) 
        VALUES ( ? )''', ( inci_type, ) )
    cur.execute('SELECT id FROM Incidents_type WHERE name = ? ', (inci_type, ))
    inci_type_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Ubication (name) 
    VALUES ( ? )''', ( Ubication, ) )
    cur.execute('SELECT id FROM Ubication WHERE name = ? ', (Ubication, ))
    Ubication_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Construction_Incidents
        (date, type_id, Fatality, Injury, Ubication_id, Latitude, Longitude) 
        VALUES ( ?, ?, ?, ?, ?, ?, ? )''', 
        ( inci_date, inci_type_id, fatality, injury, Ubication_id, latitude , longitude ) )

    conn.commit()


