valorAno = 0

def dataMagica(data, mes, ano):

    global valorAno

    if 1900 <= ano < 2000:
        valorAno = ano - 1900

    if ano >= 2000:
        valorAno = ano - 2000

    if (data * mes) == valorAno:
        return f"{data}/{mes}/{valorAno} é mágico"
    else:
        return 'não é um dia mágico'

print(dataMagica(10, 4, 1940))


