# vamos a tesear algunasd cuestiones relacionadas a estructuras de datos


vault = list()


count = 0

while True:
    inp = input('A ver badre, anda tirandome numeros....')
    inp = float(inp)
    vault.append(inp)
    count = count + 1
    
    if count == 10 : break

vault.sort()

print(vault, inp, sum(vault), len(vault))

