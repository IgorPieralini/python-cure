def maximo(x, y, imprime=False):
    max_valor = x if x > y else y
    if imprime:
        print(max_valor)
    return max_valor

print(maximo(1, 2))
maximo(7, 20, True)