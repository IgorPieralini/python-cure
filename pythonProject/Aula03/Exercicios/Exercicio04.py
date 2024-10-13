anoatual = 2024
anonascimeto = int(input("Digite o ano em que vcoê nasceu: "))

idade = anoatual - anonascimeto
print("Sua idade é", idade)

if idade >= 16:
    print("Você já pode votar")
else:
    print("Você não pode votar")

if idade >= 18:
    print("Você já pode dirigir")
else:
    print("Você não pode dirigir")