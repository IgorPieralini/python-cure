while True:

    print("=================")
    print("Programa iniciado")
    print("=================")

    soma = 0
    contador = 0

    # RECEBENDO INFORMAÇÕES
    for i in range(0, 10):
        numero = int(input("Digite um valor: "))
        soma = soma + numero
        contador = contador + 1

    # ESCREVENDO TODAS AS INFORMAÇÕES
    print("===============================")
    print("Foram digitador um total de", contador, "números")
    print("A soma entre eles é:", soma)
    print("===============================")

    # PROGRAMA REINICIADO
    print("======== RELOAD ========")
