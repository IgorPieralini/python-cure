from random import randint

# Criando a matriz 12x12 com números inteiros aleatórios de 0 a 10
matriz = []
for num_linha in range(12):
    linha = []
    for num_coluna in range(12):
        linha.append(randint(0, 10))  # Números aleatórios de 0 a 10
    matriz.append(linha)

# Lendo a operação desejada
operacao = input().strip().upper()

# Função para imprimir a matriz
def imprimir_matriz(teste):
    for linha in teste:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()

# Imprimindo a matriz original
print("Matriz criada:")
imprimir_matriz(matriz)

# Inicializando a soma e a contagem de elementos
soma = 0
contador = 0

# Calculando a soma ou média dos elementos acima da diagonal secundária
for i in range(12):
    for j in range(12):
        # Elementos acima da diagonal secundária: j < 11 - i
        if j < 11 - i:
            soma += matriz[i][j]
            contador += 1

# Calculando e mostrando o resultado
if operacao == 'S':
    print(f"Resultado da conta: {soma}")
elif operacao == 'M':
    if contador > 0:
        media = soma // contador  # Média como inteiro
        print(f"Resultado da conta: {media}")
    else:
        print("\nNão há elementos acima da diagonal secundária para calcular a média.")
else:
    print("\nOperação inválida! Digite 'S' ou 'M'.")