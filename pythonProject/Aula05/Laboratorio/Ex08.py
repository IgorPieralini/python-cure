linhas = int(input("Digite a quantidade de linhas: "))

t = 1
for i in range (linhas):
    print(t, t + 1, t + 2, "PIM")
    i += 1
    t += 4
