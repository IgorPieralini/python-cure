maior = 0
comparador = 0

# PEGANDO OS NÚMEROS
for i in range(0, 6):
    numero = int(input("Digite um número: "))

    # VERIFICAÇÃO DO MAIOR VALOR
    if  numero > comparador:
        comparador = numero

# IMPRESSÃO DO MAIOR VALOR
print("============================")
print("O maior valor é:", comparador)
print("============================")

