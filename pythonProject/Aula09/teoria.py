lista = "hello", 6.7, 5, [1, 2]
print(lista[3])
print(lista[3][0])

for i in range (0, 2):
    print(lista[3][i], end=" ")


# ---------------------------------------------------
print(end=print())
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(A[1][1])

for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        print(A[linha][coluna], end=" ")
    print()

for linha in A:
    for elemento in linha:
        print(elemento, end=" ")
    print()

