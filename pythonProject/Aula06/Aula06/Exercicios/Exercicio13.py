import math
def exponencial(n):


    # Inicializa b como o menor valor possível, que é 2
    b = 2

    # Loop para encontrar o menor b possível
    while b <= n:
        # Calcula k como o logaritmo de n na base b
        k = round(math.log(n, b))

        # Verifica se b^k é igual a n
        if b ** k == n:
            return b, k

        # Incrementa b para testar o próximo valor
        b += 1

print(exponencial(20))
