import random

# Cria o arquivo numeros.txt com 100 números aleatórios
def criar_arquivo_numeros():
    numeros = [str(random.randint(0, 1000)) for _ in range(100)]  # Gera 100 números aleatórios
    with open('numeros.txt', 'w') as numeros_file:
        numeros_file.write(' '.join(numeros))  # Escreve os números em uma única linha, separados por espaço

# Função para calcular a somatória dos números no arquivo numeros.txt
def somar_numeros_do_arquivo():
    with open('numeros.txt', 'r') as numeros_file:
        linha = numeros_file.readline()  # Lê a única linha do arquivo
        numeros = map(int, linha.split())  # Converte os números de string para inteiro
        return sum(numeros)  # Retorna a soma

# Cria o arquivo
criar_arquivo_numeros()

# Calcula e exibe a somatória
soma = somar_numeros_do_arquivo()
print(f"A somatória dos números no arquivo é: {soma}")