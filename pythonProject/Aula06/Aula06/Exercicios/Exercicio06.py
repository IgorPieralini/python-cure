from math import sqrt


def equacao(x, y, z):
    return (sqrt(x) + sqrt(y) + sqrt(z)) + (x + y) / 2 + (y + z) / 2 + (x + z) / 2

print(equacao(4, 9, 16))