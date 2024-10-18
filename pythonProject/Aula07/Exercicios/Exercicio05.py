import statistics
def analise(lista):
    maior = 0
    menor = 10000000000
    soma = 0
    contador = 0

    for ix in lista:
        contador = contador + 1
        soma = soma + ix

    med = soma/contador

    mediana = statistics.median(lista)

    for i in lista:
        numero = lista[i]
        if (numero > maior):
            maior = numero

    for l in lista:
        numero - lista[i]
        if (numero < menor):
            menor = numero

    return med, mediana, menor, maior
