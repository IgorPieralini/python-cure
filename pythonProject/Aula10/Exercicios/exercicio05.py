def anagrama(plv1, plv2):
    letra1 = {}
    letra2 = {}

    for letra in plv1:
        letra1[letra] = letra1.get(letra, 0) + 1

    for letra in plv2:
        letra2[letra] = letra2.get(letra, 0) + 1

    print(letra1, letra2)

    if letra1 == letra2:
        return 'são anagramas'
    else:
        return 'não são anagramas'

print(anagrama('estante', 'setenta'))