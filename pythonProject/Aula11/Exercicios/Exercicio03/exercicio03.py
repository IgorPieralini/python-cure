import random

# Função para criar o arquivo numeros.txt com 100 números aleatórios
def criar_arquivo_numeros():
    numeros = [str(random.randint(0, 1000)) for _ in range(100)]  # Gera 100 números aleatórios
    with open('numeros.txt', 'w') as numeros_file:
        numeros_file.write(' '.join(numeros))  # Escreve os números em uma única linha, separados por espaço

# Função para ler os números do arquivo e salvar em uma lista
def ler_numeros():
    with open('numeros.txt', 'r') as numeros_file:
        linha = numeros_file.readline()  # Lê a única linha do arquivo
        num = list(map(int, linha.split()))  # Converte os números de string para inteiro
    return num

# Função para remover duplicatas da lista
def remover_duplicatas(num):
    num_unicos = list(set(num))  # Usa set para remover duplicatas e converte de volta para lista
    return num_unicos

# Função para gravar os números únicos em numeros_unicos.txt
def gravar_numeros_unicos(num_unicos):
    with open('numeros_unicos.txt', 'w') as numeros_unicos_file:
        numeros_unicos_file.write(' '.join(map(str, num_unicos)))  # Escreve os números únicos em uma linha

# Cria o arquivo com números aleatórios
criar_arquivo_numeros()

# Lê os números do arquivo
numeros = ler_numeros()

# Remove duplicatas
numeros_unicos = remover_duplicatas(numeros)

# Grava os números únicos em um novo arquivo
gravar_numeros_unicos(numeros_unicos)

print("Os números únicos foram gravados em numeros_unicos.txt.")