def media(lista):
    soma = 0
    contador = 0

    for ix in lista:
        contador = contador + 1
        soma = soma + ix

    med = soma/contador
    return med