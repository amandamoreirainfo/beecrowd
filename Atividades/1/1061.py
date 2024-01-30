
entradaInicial = input("Informe a Data do Evento: ")
horaInicial = input("Informe o Momento no qual o Evento vai Iniciar: ")
entradaFinal = input("Informe a Data Final do Eveneto: ")
horaFinal = input("Informe a Hora que o Evento vai terminar: ")


diaInicial = int(entradaInicial.split()[1])
horaInicial, minutoInicial, segundoInicial = map(int, horaInicial.split(":"))

diaFinal = int(entradaFinal.split()[1])
horaFinal, minutoFinal, segundoFinal = map(int, horaFinal.split(":"))

tempoInicialSegundos = segundoInicial + minutoInicial * 60 + horaInicial * 3600 + diaInicial * 24 * 3600
tempoFinalSegundos = segundoFinal + minutoFinal * 60 + horaFinal * 3600 + diaFinal * 24 * 3600
duracaoSegundos = tempoFinalSegundos - tempoInicialSegundos

dias = duracaoSegundos // (24 * 3600)
horas = (duracaoSegundos % (24 * 3600)) // 3600
minutos = (duracaoSegundos % 3600) // 60
segundos = duracaoSegundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")

