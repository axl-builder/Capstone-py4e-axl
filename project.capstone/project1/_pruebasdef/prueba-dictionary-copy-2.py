# vamos a tesear algunasd cuestiones relacionadas a estructuras de datos


vault = list()
dicto = dict()

count = 0


while True:
    inp = input('decime 10 nombres que despues vamos a contabilizar cuales se repiten  :')
    vault.append(inp)

    count = count + 1
    if count == 10 : break


print('bueno mira, de lista tenes lo siguiente: ', vault)


# vamos a contabilizar, los nombres repetidos o no dentro de la lista


for itevar in vault:
    dicto[itevar] = dicto.get(itevar,0) + 1 # esta formula es fundamental

print(dicto)