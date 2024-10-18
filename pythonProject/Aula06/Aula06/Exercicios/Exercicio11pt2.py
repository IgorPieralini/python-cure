def funcao(i, a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    if i == 1:
        print(a, b, c)
    elif i == 2:
        print(c, b, a)
    elif i == 3:
        print(a, c, b)

funcao(1, 3, 2, 1)