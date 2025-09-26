# vamos a tesear algunasd cuestiones relacionadas a estructuras de datos


vault = dict()


count = 0

vault['axel'] = 33
vault['ivonne'] = 35
vault['orson'] = 6
vault['nairobi'] = 5

while True:
    inp = input('badre, carga una key (osea llave)')
    onp = input('badre, carga un value (osea valor)')
    onp = int(onp)
    vault.get(inp, onp)

    count = count + 1
    
    if count == 5 : break


print(vault)

