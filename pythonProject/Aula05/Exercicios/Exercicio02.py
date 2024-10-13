linha = int(input())
coluna = int(input())

while True:
    if linha > 0 and coluna > 0:
        for l in range(linha):
            for c in range(coluna):
                if l == 0 or l == linha - 1 or c == 0 or c == coluna - 1:
                    print("*", end="")
                else:
                    print(" ", end="")

            print()