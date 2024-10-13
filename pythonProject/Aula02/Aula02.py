import colorama
from colorama import init
init()

# Comentário de Uma linha somente

"""

Comentário de várias linhas!!



print(10 < 10) # False
print(9 != 5) # True
print(9 == 5) # False
print(5 > 5) # False

a = 9
b = 5

print(a == b) # False
print(a > b) # True
print(a < b) # False

"""

# IF; ELSE; LER O QUE USUÁRIO DIGITA

c = int(input("Digite um núemro: "))

if(c > 0):
    print(c, " É maior do que 0")
    print(colorama.Fore.BLUE + "Este núemero é positivo")
else:
    print(c, " É menor ou igual a 0")
    print(colorama.Fore.RED + "Este número é 0 ou negativo")



