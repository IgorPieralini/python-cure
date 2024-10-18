from random import randint

def lancamento():
    return randint(1, 6) + randint(1, 6)

lancamentos = {}
for i in range(1000):
    valor = lancamento()
    lancamentos[valor] = lancamentos.get(valor, 0) + 1

print('Lançamentos:')
print(lancamentos)
print()
print('em 1000 lançamentos tivemos as seguintes porcentagens')

for chave, valor in lancamentos.items():
    print(f'{chave} : {valor/1000 * 100:.f}%')