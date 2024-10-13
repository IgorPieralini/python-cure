numero = int(input("Digite um número inteiro: "))

if  numero > 0:
    numero_digitos = 0

    while numero > 0:
        numero =  numero // 10
        numero_digitos = numero_digitos + 1

    print(numero_digitos)