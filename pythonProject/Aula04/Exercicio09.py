# N DEFINE QUANDO O LOOPING VAI PARAR
n = int(input("Digite um valor: "))
inteiro = 1

equacao = 0
reposta = 0

for i in range(0, n):
    equacao = 1 / n
    reposta = reposta + equacao

    # CALCULO : 1 / n + 1 / (n + 1) + 1 / (n + 2) ..........

# ESCREVENDO TODAS AS INFORMAÇÕES
print(reposta)