import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
import json
#import pandas as pd
#manera con sql fuerte

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

dicto_sum = dict()

cur.execute( """
SELECT 
    strftime('%Y-%m', c.date) AS anio_mes,
    u.name AS ubicacion,
    COUNT(*) AS cantidad,
    SUM(CAST(c.Fatality AS INTEGER)) AS suma_fatality,
    SUM(CAST(c.Injury AS INTEGER)) AS suma_injury
FROM Construction_Incidents c
JOIN Ubication u ON c.Ubication_id = u.id
GROUP BY anio_mes, u.name
ORDER BY anio_mes, u.name;

""")

rows = cur.fetchall()

print(json.dumps(rows, indent=4))

for itevar in rows:
    itevarsum = itevar[4] + itevar[3]
    print(itevar)

barrios = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']


agrupado = {}
for fecha, barrio, *_ , numero_final in rows:
    if fecha not in agrupado:
        agrupado[fecha] = {}
        print('a',agrupado)
    agrupado[fecha][barrio] = numero_final
    print('b',agrupado)

print('c',agrupado, '\n')



# Convertimos a la lista final
resultado = []
for fecha in sorted(agrupado.keys()):
    fila = [fecha] + [agrupado[fecha].get(b, 0) for b in barrios]
    print('fila', fila)
    print(sum(fila))
    resultado.append(fila)



var = open('colchart2.js','w')
var.write("testo = [ ['Date', 'Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island, Incidents count']")
for itevar in resultado:
    var.write(",\n"+str(itevar))

var.write('\n];')



# Definimos el orden de los barrios que nos interesan

