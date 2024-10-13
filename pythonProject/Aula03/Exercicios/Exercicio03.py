intsexo = int(input("Digite 1 Para Homem, e 2 para mulher: "))
altura = float(input("Digite sua altura: "))

sexo = "sexo"

if intsexo == 1:
    sexo = "Masculino"
    idhhomem = (72.7 * altura) - 58

    print("Seu peso ideal é:", idhhomem)
else:
    if intsexo == 2:
        sexo = "Feminino"
        idhmulher = (62.1 * altura) - 44, 7

        print("Seu peso ideal é:", idhmulher)
    else:
        print("Valor inválido, reinicie o programa")



