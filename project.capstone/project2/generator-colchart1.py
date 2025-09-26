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

dicto_sum = dict()

cur.execute('SELECT ci.Fatality, ci.Injury, u.name AS ubication FROM Construction_Incidents ci JOIN Ubication u ON ci.Ubication_id = u.id')
ordenado = dict()
for itevar in cur :
    fatality = int(itevar[0])
    injury = int(itevar[1])
    ubicacion = itevar[2]
    print(fatality)
    print(injury)
    print(ubicacion)

    if ubicacion not in ordenado:
        ordenado[ubicacion] = {"fatalities": 0, "injuries": 0}

    ordenado[ubicacion]["fatalities"] += fatality #guarda aca. mejorar en manejo de estructuras de datos.
    ordenado[ubicacion]["injuries"] += injury #guarda aca. mejorar en manejo de estructuras de datos.


print(ordenado)
print(ordenado.items())
print(ordenado.keys())
print(ordenado.values())



var = open('colchart.js','w')
var.write("testo = [ ['Ubication', 'Fatality', 'Injury']")

for a,b in ordenado.items():
    fatalities = b['fatalities']
    injuries = b['injuries']

    print(a)
    print(fatalities)
    print(injuries)

    var.write(",\n['"+str(a)+"'"', '+str(fatalities)+', '+str(injuries)+"]")

var.write('\n];')