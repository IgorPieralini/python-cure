tamanho_tab = int(input("Tamanho da tabela: "))

if tamanho_tab > 0:
    for linha in range(tamanho_tab):
        for coluna in range(tamanho_tab):
            if(linha - coluna) <= 0:
                print("@", end="")
            else:
                print("$", end="")
        print()