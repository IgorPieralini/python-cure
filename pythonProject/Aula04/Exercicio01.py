a = int(input("Digite o valor máximo: "))
i = 0

print("====================")
print("Números pares até", a)
print("====================")

# IMPRIMINDO OS PARES
while(i < a):
    valor = i % 2
    if (valor == 0):
        print(i)

    i = i + 1;