import colorama

tabuleiro = int(input())

if tabuleiro > 0:
    for linha in range(tabuleiro):
        for coluna in range(tabuleiro):
            if(linha + coluna) % 2 == 0:
                print(colorama.Back.LIGHTWHITE_EX + " ", end="")
            else:
                print(colorama.Back.BLACK + " ", end="")
        print(colorama.Back.RESET)