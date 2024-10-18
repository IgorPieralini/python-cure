valorAno = 0


def dataMagica():
    data = 0
    mes = 0
    ano = 1900

    while ano < 2000:
        data = data + 1

        if data + 1 == 32:
            data = 1
            mes = mes + 1

        if mes + 1 == 14:
            data = 1
            mes = 1
            ano = ano + 1

        if 1900 <= ano < 2000:
            valorAno = ano - 1900

        if ano >= 2000:
            valorAno = ano - 2000

        if (data *  mes == valorAno):
            print(f'{data}/{mes}/{ano} é mágico')


print(dataMagica())


