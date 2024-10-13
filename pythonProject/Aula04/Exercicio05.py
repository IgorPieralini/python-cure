while True:
    numero = int(input("Digite um número de 1 a 10: "))

    # VALIDAÇÃO DO NÚMERO DIGITADO
    if numero < 1 or numero > 10:
        print("Número inválido, Tente novamente!!")
    else:

        # ESCREVENDO TODAS AS INFORMAÇÕES
        print("============================================")
        print("Número aceito, iremos fazer o PIX em breve!!")
        print("         O programa será encerrado          ")
        print("============================================")
        break
