coidgop = int(input("Digite o código do Produto: "))
entradap = (input("Digite a da de entrada do Produto: "))
nomep = (input("Digite o nome do Produto: "))

a = "regiao"

if coidgop == 1:
    a = "Sul"
elif coidgop == 2:
    a = "Norte"
elif coidgop == 3:
    a = "Leste"
elif coidgop == 4:
    a = "Oeste"
elif coidgop == 5 or coidgop == 6:
    a = "Nordeste"
elif coidgop == 7 or coidgop == 8 or coidgop == 9:
    a = "Sudeste"
elif 10 <= coidgop <= 20:
    a = "Centro-Oeste"
elif 25 <= coidgop <= 30:
    a = "Nordeste"
else:
    a = "Produto Importado"

print("A região é:", a)
print("a Data de entrada é:", entradap)
print("o nome é:", nomep)
