from random import randint, random

lista_inteiros = [randint(1, 100) for i in range(10)]
lista_reais = [random()*100 for i in range(5)]
lista_strings = ["a", "b", "c", "d", "c", "e", "f", "g"]

lista_completa1 = [lista_inteiros, lista_reais, lista_strings]
lista_completa2 = lista_inteiros + lista_reais + lista_strings

print(lista_completa1)
print(lista_completa2)