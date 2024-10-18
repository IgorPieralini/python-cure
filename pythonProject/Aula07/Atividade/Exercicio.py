lista1 = []
lista2 = []
lista3 = []
soma = 0

for i in range(0, 10):
    if i % 2 == 0:
        lista1.append(i)
    else:
        lista2.append(i)

    lista3.append(lista1[i] + lista2[i])

soma = lista1 + lista2
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", soma)

