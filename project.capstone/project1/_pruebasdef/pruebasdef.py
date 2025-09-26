dicto = {
    'a': (999, 2001, "arriba"),
    'd': (305, 2001, "abajo"),
    'e': (88,  2002, "arriba"),
    'f': (654, 2002, "abajo"),
    'g': (777, 2003, "arriba"),
    'h': (432, 2003, "abajo"),
    'i': (100, 2004, "arriba"),
    'j': (555, 2004, "abajo"),
}

agrupado = {}

for _, (valor1, anio, pos) in dicto.items():
    if anio not in agrupado:
        agrupado[anio] = {"arriba": None, "abajo": None}
    agrupado[anio][pos] = valor1

for anio in sorted(agrupado):
    print(anio, agrupado[anio]["arriba"], agrupado[anio]["abajo"])

