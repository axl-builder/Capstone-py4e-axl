import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import json

# 'El objjetivo de este programa es el de tomar los
#  datos de la base de datos generada con spider.py 
# y estructurar los datos para un determinado chart
# en este caso, column chart
# Donde las barras sean 2 y sean injuries y fatalities
# Donde el eje X sea ubicaciones
# Donde el eje Y sea numerico, en relacion a injuries y fatalities'

# '       ['Ubications', 'Fatalities', 'Injuries'],
# '       ['Manhattan', 8000, 23.3],
# '       ['Bronx', 24000, 4.5],
# '       ['Brooklyn', 30000, 14.3],
# '       ['Staten Island', 60000, 13.1] 

  
conn = sqlite3.connect('Construction-Related_Incidents.sqlite')
cur = conn.cursor()

datos = cur.execute('''
SELECT it.name AS Incident_Type,
       SUM(CAST(ci.Fatality AS INTEGER)) AS Total_Fatalities,
       SUM(CAST(ci.Injury AS INTEGER)) AS Total_Injuries
FROM Construction_Incidents ci
JOIN Incidents_type it ON ci.type_id = it.id
GROUP BY it.name
ORDER BY Total_Fatalities DESC, Total_Injuries DESC;
''')

lista = list()

#construyendo dona 1 , construyendo dona 2

var = open('donut.js','w')
var.write("testdonut = [ ['Construction incident', 'Fatalities count'],")



for itevar in datos:
    print(itevar)
    print(itevar[0])
    print(itevar[1])
    print(itevar[2])

    var.write("\n[ "+"'"+itevar[0]+"', "+str(itevar[1])+" ],")

var.write('\n];')
var.close()

datos = cur.execute('''
SELECT it.name AS Incident_Type,
       SUM(CAST(ci.Fatality AS INTEGER)) AS Total_Fatalities,
       SUM(CAST(ci.Injury AS INTEGER)) AS Total_Injuries
FROM Construction_Incidents ci
JOIN Incidents_type it ON ci.type_id = it.id
GROUP BY it.name
ORDER BY Total_Fatalities DESC, Total_Injuries DESC;
''')

var = open('donut2.js','w')
var.write("testdonut = [ ['Construction incident', 'Injuries count'],")

for itevor in datos:
    print(itevor)
    print(itevor[0])
    print(itevor[1])
    print(itevor[2])

    var.write("\n[ "+"'"+itevor[0]+"', "+str(itevor[2])+" ],")

var.write('\n];')
var.close()