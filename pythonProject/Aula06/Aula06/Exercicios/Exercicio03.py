def maximo(x, y):

    if x > y:
        return "O primeiro valor é maior"
    elif x < y:
        return "O segundo valor é maior"
    else:
        return "Os valores são iguais"

print(maximo(50, 40))