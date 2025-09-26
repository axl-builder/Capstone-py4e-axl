import sqlite3
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse


sqlconect = sqlite3.connect('database.sqlite')
cur = sqlconect.cursor()


var = open('capstone.js','w')
var.write("gline = [ ['año', 'National', 'Real State']")


cur.execute('SELECT Year, Industry_Jobs, Source FROM Realstate_Jobs')
ordenado = dict()
for itevar in cur :
    año = itevar[0]
    valor = itevar[1]
    tipo = itevar[2]
    print(año)
    print(valor)
    print(tipo)
    if año not in ordenado:
        ordenado[año] = {"National": None, "Real State": None} 
    ordenado[año][tipo] = valor


print(ordenado)



for a,b in ordenado.items():
    var.write(",\n['"+str(a)+"'"', '+str(b['National'])+', '+str(b['Real State'])+']')

var.write('\n];')

