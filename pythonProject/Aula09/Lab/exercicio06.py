def criar_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(2):
            num = int(input(f"Digite o elemento da linha {i} e coluna {j}: "))
            linha.append(num)
        matriz.append(linha)
    return matriz


# Função para contar elementos maiores que 10 e criar a matriz modificada
def processar_matriz(matriz):
    contador_maiores_que_10 = 0
    matriz_modificada = []

    for i in range(4):
        linha_modificada = []
        for j in range(2):
            if matriz[i][j] > 10:
                print(f"{matriz[i][j]} é maior que 10!")
                contador_maiores_que_10 += 1
                linha_modificada.append(0)
            else:
                linha_modificada.append(matriz[i][j])
        matriz_modificada.append(linha_modificada)

    return contador_maiores_que_10, matriz_modificada


# Função para imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


# Main
matriz = criar_matriz()
print("Matriz original:")
imprimir_matriz(matriz)
print()

contador, matriz_modificada = processar_matriz(matriz)

print(f"No total, {contador} elementos são maiores que 10!\n")
print("Matriz sem os números maiores que 10:")
imprimir_matriz(matriz_modificada)