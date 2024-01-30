
linha = input("Informe os Valoes: ")

horaInicial, minutoInicial, horaFinal, minutoFinal = linha.split()

horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)

horaDia = horaFinal - horaInicial
minutoDia = minutoFinal - minutoInicial

totalMinutosInicial = horaInicial * 60 + minutoInicial
totalMinutosFinal = horaFinal * 60 + minutoFinal

duracaoMinutos = totalMinutosFinal - totalMinutosInicial

if duracaoMinutos <= 0:
    duracaoMinutos += 24 * 60

horas = duracaoMinutos // 60
minutos = duracaoMinutos % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
