horai = int(input("Digite a hora inicial:"))
minutoi = int(input("Digite o minuto inicial:"))
horaf = int(input("Digite a hora final:"))
minutof = int(input("Digite o minuto final:"))

horas = horaf - horai
minutos = minutof - minutoi

if minutoi > minutof:
    minutos = (60 - minutoi) + minutof
    if horas < 24:
        horas = horas + 1

if horai > horaf:
    horas = (24 - horai) + horaf
    if minutos < 60 & minutoi > minutof:
        horas = horas - 1

if minutos == 60:
    minutos = 0
    horas = horas + 1

print("O jogo durou", horas, "hora(s) e", minutos, "minutos(s)")