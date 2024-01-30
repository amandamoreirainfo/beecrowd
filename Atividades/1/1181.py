

X = int(input("Informe um Número: "))
operacao = input("Informe um Número: ")
A = []


for i in range(12):
    A.append([])

for i in range(12):
    for j in range(12):
        z = float(input("Informe um Número: "))
        A[i].append(z)

if operacao == "S":
    soma = 0
    for k in range(12):
        soma = soma + k
    print(soma)

if operacao == "M":
    media = 0
    soma = 0
    for y in range(12):
        soma = soma + y
    media = soma / 12
    print(f"{media}")