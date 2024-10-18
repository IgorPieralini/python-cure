def caracteresunic(frase):
    caracteres = {}
    for caractere in frase:
        caracteres[caractere] = 1
    return (len(caracteres))

print(caracteresunic('hello, world'))