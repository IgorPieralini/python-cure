numero = int(input("Número inteiro: "))

if numero > 0:
    a = 0
    b = 1
    c = 0

    while b < numero:
        c = a + b
        a = b
        b = c
        if b == numero:
            print("O número pertence")
        else:
            print("Não pertence")


True
