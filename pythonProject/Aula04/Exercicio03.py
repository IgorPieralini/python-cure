numero = int(input("Qual tabuada deseja: "))

i = 0

print("======================")
print("Está é a Tabuada do", numero)
print("======================")

# IMPRIMINDO TABUADA
for i in range(0, 10 + 1):
    resposta = numero * i
    print(numero, "X", i, "=", resposta)
    i = i + 1