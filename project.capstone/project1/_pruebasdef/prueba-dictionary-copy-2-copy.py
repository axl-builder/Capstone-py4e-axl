# vamos a tesear algunasd cuestiones relacionadas a estructuras de datos


text = input('introduzca el texto del cual precise contabilizar sus palabras individualmente  :')
texto = text.split( )

print(texto)

dicto = dict()

for itevar in texto:
    dicto[itevar] = dicto.get(itevar, 0) + 1

print(dicto)

for itedict in dicto:
    print('key', itedict)
    print('value', dicto[itedict])

print(list(dicto))
print(list(dicto.keys()))
print(list(dicto.values()))
print(list(dicto.items()))