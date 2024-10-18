def aptoADoar(sexo, massa):

    if  sexo == 'M':
        if massa >= 50:
            return "Você está apta para doar"
        else:
            return 'Você não pode doar'
    elif sexo == 'H':
        if massa >= 60:
            return "Você está apta para doar"
        else:
            return 'Você não pode doar'
    else:
        return 'Este sexo não existe'

print(aptoADoar('M', 40))
print(aptoADoar('M', 60))
print(aptoADoar('H', 40))
print(aptoADoar('H', 60))
print(aptoADoar('CIS', 40))