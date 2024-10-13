media = 0
aprovados = 0
reprovados = 0
valor = 0
notas = 0

# COMEÇA O LOOPING PARA DIGITAR 80 NOTAS
for i in range(0, 80):
    nota = float(input("Digite a nota: "))
    notas = notas + 1

    # APROVADO => 6
    if nota >= 6:
        aprovados = aprovados + 1
    # REPROVADO < 6
    else:
        reprovados = reprovados + 1

    valor = valor + nota

    # MÉDIA NOTAS
    media = valor / notas

# ESCREVENDO TODAS AS INFORMAÇÕES
print("A média das notas é: ", media)
print("O total de alunos aprovados foram: ", aprovados)
print("O total de alunos reprovados foram: ", reprovados)


