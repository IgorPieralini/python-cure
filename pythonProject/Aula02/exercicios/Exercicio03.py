print("---------------------")
print("Domingo: 0")
print("Segunda: 1")
print("Terça: 2")
print("Quarta: 3")
print("Quinta: 4")
print("Sexta: 5")
print("Sábado: 6")
print("---------------------")

diaDasemana = int(input("Digite o dia que você quer: "))

if (diaDasemana % 7) == 0:
    print("É Domingo")
if (diaDasemana % 7) == 1:
    print("É Segunda")
if (diaDasemana % 7) == 2:
    print("É Terça")
if (diaDasemana % 7) == 3:
    print("É Quarta")
if (diaDasemana % 7) == 4:
    print("É Quinta")
if (diaDasemana % 7)  == 5:
    print("É Sexta")
if (diaDasemana % 7) == 6:
    print("É Sábado")

