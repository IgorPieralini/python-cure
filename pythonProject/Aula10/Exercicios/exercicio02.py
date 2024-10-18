from random import randint

lista = []
dicionario = {}

for i in range (100):
    numero = randint(0, 21)
    lista.append(numero)

lista.sort()

for numero in lista:
    dicionario[numero] = dicionario.get(numero, 0) + 1

for chave, valor in dicionario.items():
    print(f"{chave} : {valor}")
print(lista)
print(dicionario)