# generar un diccionario en base a un texto pre existente. en el cual esten contabilizada cada palabra del texto

text = input('ingrese nombre de archivo :')
handle = open(text)

dicto = dict()
for itevar in handle:
    itevar = itevar.rstrip()
    itevar = itevar.split()
    for palabras in itevar:
        dicto[palabras] = dicto.get(palabras, 0) + 1
        print(palabras)

print(list((dicto.items())))

palabramax = None
numeromax = None

for a,b in dicto.items():
    if numeromax is None or b > numeromax:
        palabramax = a
        numeromax = b
        

print(palabramax, numeromax)







