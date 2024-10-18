# Lê os números do arquivo pares.txt e grava os múltiplos de 4 em multiples_de_4.txt

# Abre o arquivo pares.txt para leitura e o novo arquivo para escrita
with open('pares.txt', 'r') as pares_file, open('multiples_de_4.txt', 'w') as multiples_file:
    # Itera sobre cada linha do arquivo pares.txt
    for line in pares_file:
        numero = int(line.strip())  # Converte a linha para um número inteiro
        if numero % 4 == 0:  # Verifica se o número é múltiplo de 4
            multiples_file.write(f"{numero}\n")  # Grava no novo arquivo