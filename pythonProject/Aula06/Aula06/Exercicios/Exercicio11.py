

def funcao(i, a, b, c):
    maior = 0
    intermediario = 0
    menor = 0

    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    elif c < a  and c < b:
        menor = c

    if a > b and a > c:
        maior = a
    elif b > a and b > c:
        maior = b
    elif c > a and c > b:
        maior = c

    if a < b < c:
        intermediario = b
    elif c < b < a:
        intermediario = b
    elif a < c < b:
        intermediario = c
    elif b < c < a:
        intermediario = c
    elif b < a < c:
        intermediario = a
    else:
        intermediario = a

    print(menor, intermediario, maior)

    if i == 1:
        print(menor, intermediario, maior)
    elif i == 2:
        print(maior, inter, menor)
    elif i == 3:
        print(intermediario, maior, menor)


funcao(1, 3, 2, 1)

