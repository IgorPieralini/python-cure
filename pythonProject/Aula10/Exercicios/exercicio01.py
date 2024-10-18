def procurachave(dicionario, valor):
    print("Procurando chave com valor ", valor)
    chaves = []

    for chave in dicionario:
        if dicionario[chave] == valor:
            chaves.append(chave)
    return chaves

dicionario = {'alpha': 1, 'bravo': 2, 'charlie': 1, 'delta': 3, 'echo': 1}
print(procurachave(dicionario, 1))
