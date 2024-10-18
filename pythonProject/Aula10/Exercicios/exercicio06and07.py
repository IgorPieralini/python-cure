from random import randint


def cartao():
    cartela = {}
    letras = 'BINGO'
    limites = [15, 30, 45, 60, 75]

    for i in range(5):
        letra = letras[i]
        limite = limites[i]
        cartela[letra] = []

        while len(cartela[letra]) < 5:
            numero = randint(limite - 14, limite)
            if  numero not in cartela[letra]:
                cartela[letra].append(numero)

    return cartela

def imprime_cartela(cartela):
    for chave, valor in cartela.items():
        print(f'{chave} : {valor}')

cartela = cartao()
print(imprime_cartela(cartela))
