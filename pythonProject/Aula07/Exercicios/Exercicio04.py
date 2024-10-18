lista_carros = []
lista_consumo = []
consumo_carros = []
economico = 1
carro_economico = ''



for i in range(0, 5):
    nome_carro = input()
    lista_carros.append(nome_carro)


for y in range(0, 5):
    consumo_carro = int(input())
    consumo_carros.append(consumo_carro)

    if consumo_carro > economico:
        economico = consumo_carro
        carro_economico = lista_carros[y]





    if(1000 % consumo_carro == 0):
        lista_consumo.append(int(1000 / consumo_carro))
    elif(1000 % consumo_carro == 1):
        lista_consumo.append(int(1000 / consumo_carro))
    else:
        lista_consumo.append(int((1000 / consumo_carro) + 1))



print(carro_economico)

for t in range(0, 5):
    print(lista_consumo[t])


