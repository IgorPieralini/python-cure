quantidade = int(input("Digite a quantidade de entrada: "))
primos = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero > 1: # TEM QUE SER MAIOR QUE 1
        primo = True

        for j in range(2, numero): # PEGO TODOS OS NÚERMOS 2 A ATÉ NUMERO
            if numero % j == 0:
                primo = False
        if primo == True:
            primos += 1

print(f"Você digitou {primos} números primos de um total de {quantidade} números")