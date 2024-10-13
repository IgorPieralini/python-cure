digitado = 0
valor = 0
# INFORMAÇÕES PARA O USUÁRIO
print("=========================")
print("Para sair basta digitar 0")
print("=========================")

while True:
    numero = int(input("Queremos ler um número: "))

    digitado = digitado + 1

    valor = valor + numero

    # FINALIZANDO LOOPING
    if(numero == 0):

        # ESCREVENDO TODAS AS INFORMAÇÕES
        print("========================================")
        print("Foram digitados um total de", (digitado-1), "Valores")
        print("A soma deles é:", valor)
        print("A média destes números é:", (valor / (digitado - 1)))
        print(" Encerrando Programa  ")
        print("========================================")

        # PARANDO
        break


