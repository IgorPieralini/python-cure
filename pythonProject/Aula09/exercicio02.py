from random import randint

matriz = []
for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(("%3d" % (randint(1, 100))))
    matriz.append(linha)

def imprimir_matriz(teste):
    for linha in teste:
        for elemento in linha:
            print(elemento, end=" ")
        print()

def imprimir_coluna(teste, n_coluna):
    for linha in teste:
        print("%3d" % teste[linha][n_coluna])

imprimir_matriz(matriz)
imprimir_coluna(matriz, 2)