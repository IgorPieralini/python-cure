v1 = int(input("Digite o valor 1: "))

v2 = int(input("Digite o valor 2: "))
if v2 == v1:
    print("Os valores não podem ser iguais")
    v2 = int(input("Digite o valor 2: "))

v3 = int(input("Digite o valor 3: "))
if v3 == v1 or v3 == v2:
    print("Os valores não podem ser iguais")
    v3 = int(input("Digite o valor 3: "))

if v1 > v2 and v2 > v3:
    print(v1, v2, v3)
elif v2< v1 and v1 > v2:
    print(v2, v1, v3)
elif v3 > v1 and v1 > v2
    print(v3, v1, v2)
elif v1 > v3 and v3 > v2
    print(v1, v3, v2)
elif v2 > v3 and v3 > v1
    print(v2,v3, v1)
else:
    print(v3, v2, v1)