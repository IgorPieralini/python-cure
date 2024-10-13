tamanho_tab = int(input("Tamanho da tabela: "))

if tamanho_tab > 0:
    for linha in range(tamanho_tab):
        for coluna in range(tamanho_tab):

           if linha % 2 == 0:
               if coluna % 2 == 0:
                   print("$", end="")
               else:
                   print("&", end="")

           elif linha % 2 == 1:
               if coluna % 2 == 0:
                   print("%", end="")
               else:
                   print("#", end="")
        print()