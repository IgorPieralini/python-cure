# Gera números pares e ímpares de 0 a 999 e os grava em arquivos separados

# Abre os arquivos para escrita
with open('pares.txt', 'w') as pares_file, open('impares.txt', 'w') as impares_file:
    # Itera de 0 a 999
    for numero in range(1000):
        if numero % 2 == 0:
            pares_file.write(f"{numero}\n")  # Grava números pares
        else:
            impares_file.write(f"{numero}\n")  # Grava números ímpares