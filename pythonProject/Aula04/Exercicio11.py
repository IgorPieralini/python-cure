

# CONTADORES
contador = 0
contadorh = 0
contadorm = 0

# TOTAIS
idades = 0
salarios = 0

# MÉDIAS
midade = 0
msalario = 0

# LOOPING
while True:

    # SE IDADE < 0 ENCERRA O LOOPING
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        break



    sexo = int(input("Digite 1 para homem | digite 2 para mulher "))
    contador = contador + 1

    idades = idades + idade
    midade = idades / contador
    
    salario = float(input("Digite seu salário: "))
    print("======================================================")

    # SE FOR HOMEM, CONTADOR RECEBE +1
    if sexo == 1:
        contadorh = contadorh + 1
        salarios = salarios + salario
    msalario = salarios / contadorh

    # SE SALÁRIO MULHER FOR MENOR QUE 600, CONTADOR RECEBE +1
    if  (sexo == 2 and salario < 600):
        contadorm = contadorm + 1


# ESCREVENDO TODAS AS INFORMAÇÕES
print("A média de idade é:",midade)
print("A média do salário dos homens", msalario)
print("A quantidade de mulheres que ganham menos que 600 é:", contadorm)



