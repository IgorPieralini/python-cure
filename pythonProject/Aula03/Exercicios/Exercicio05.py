codigop = int(input("Digite o códgio do produto: "))

if codigop == 1:
    print("Alimento não perecivel")
elif 2 <= codigop <= 4:
    print("Alimeto perecível")
elif codigop == 5 or codigop == 6:
    print("Vestuário")
elif codigop == 7:
    print("Higiene Pessoal")
elif 8 <= codigop <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("inválido")