

N = int(input("Informe o Número de Casos de Teste: "))

valoresDentroIntervalo = 0
valoresForaIntervalo = 0 

for i in range(N):

    X = int(input("Informe um Valor: "))

    if 10 <= X <= 20:
        valoresDentroIntervalo += 1
    else:
        valoresForaIntervalo += 1

print(f"{valoresDentroIntervalo} in")
print(f"{valoresForaIntervalo} out")
