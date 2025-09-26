

dicto = dict()

dicto['a'] = 200, 2000, "arriba"
dicto['b'] = 120, 2000, "abajo"

dicto['c'] = 999, 2001, "arriba"
dicto['d'] = 305, 2001, "abajo"

dicto['e'] = 88, 2002, "arriba"
dicto['f'] = 654, 2002, "abajo"

dicto['g'] = 777, 2003, "arriba"
dicto['h'] = 432, 2003, "abajo"

dicto['i'] = 100, 2004, "arriba"
dicto['j'] = 555, 2004, "abajo"

dicto['k'] = 876, 2005, "arriba"
dicto['l'] = 246, 2005, "abajo"

dicto['m'] = 390, 2006, "arriba"
dicto['n'] = 159, 2006, "abajo"

dicto['o'] = 420, 2007, "arriba"
dicto['p'] = 423, 2007, "abajo"



organizado = {}


for _ , b in dicto.items():
    valor = b[0]
    año = b[1]
    posicion = b[2]

    print(b)
    print(valor)
    print(año)
    print(posicion)

    if año not in organizado:
        organizado[año] = {"arriba": None, "abajo": None}   
    organizado[año][posicion] = valor

sorted(organizado)
print(organizado.items())


var = open('archivo.js','w')
var.write("gline = [ ['año', 'arriba', 'abajo']")

for a,b in organizado.items():
    prueba = b['arriba']
    var.write(",\n['"+str(a)+"'"', '+str(b['arriba'])+', '+str(b['abajo'])+']')

var.write('\n];')






# hay que armar un diccionario nuevo. donde el key sea el año, y
