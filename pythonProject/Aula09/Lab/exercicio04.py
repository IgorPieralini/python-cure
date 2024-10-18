def media(lista):
    soma = 0
    contador = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
        contador = contador + 1

    media = soma / contador
    return media

print(media([5, 12, 15, 8]))
