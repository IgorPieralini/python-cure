# Lê as linhas do arquivo pares.txt, inverte a ordem e grava em invertido.txt

# Lê o arquivo pares.txt
with open('pares.txt', 'r') as pares_file:
    linhas = pares_file.readlines()  # Lê todas as linhas

# Inverte a ordem das linhas
linhas_invertidas = linhas[::-1]

# Grava o resultado em invertido.txt
with open('invertido.txt', 'w') as invertido_file:
    invertido_file.writelines(linhas_invertidas)

print("Ordem das linhas invertida e salva em invertido.txt.")