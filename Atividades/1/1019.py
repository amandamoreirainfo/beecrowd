#556

#0:9:16

N = int(input("Informe o Tempo de duração em segundos: "))


horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 60


print(f"{horas}:{minutos}:{segundos}")

