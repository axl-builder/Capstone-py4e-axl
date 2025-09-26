data = [
    ('2025-08', 'Bronx', 6, 0, 6),
    ('2025-08', 'Brooklyn', 12, 0, 6),
    ('2025-08', 'Manhattan', 11, 0, 8),
    ('2025-08', 'Queens', 9, 0, 7),
    ('2025-08', 'Staten Island', 1, 0, 0),
    ('2025-09', 'Bronx', 4, 0, 3),
    ('2025-09', 'Brooklyn', 8, 1, 3),
    ('2025-09', 'Manhattan', 9, 0, 6),
    ('2025-09', 'Queens', 3, 0, 2)
]

# Definimos el orden de los barrios que nos interesan
barrios = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens']

# Diccionario para agrupar por fecha
agrupado = {}
for fecha, barrio, *_ , numero_final in data:
    if fecha not in agrupado:
        agrupado[fecha] = {}
        print('a',agrupado)
    agrupado[fecha][barrio] = numero_final
    print('b',agrupado)
print('c',agrupado)


print('                                          ')
print('z', agrupado.keys())


# Convertimos a la lista final
resultado = []
for fecha in sorted(agrupado.keys()):
    fila = [fecha] + [agrupado[fecha].get(b, 0) for b in barrios]
    print('fila', fila)
    resultado.append(fila)

# Mostrar resultado
for r in resultado:
    print(r)
    