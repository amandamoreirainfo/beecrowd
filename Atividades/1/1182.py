

C = int(input("Informe um Número: "))
operacao = input("Informe um Número: ")
M = []


for i in range(12):
    linha = []

    for j in range(12):
        linha.append(float(input("Informe um Número:"))) 
    M.append(linha) 

soma = 0

for i in range(12):
    soma += M[i][C]


if operacao == "S":
    print(f"{soma:.1f}")

if operacao == "M":
    media = soma / 12
    print(f"{media:.1f}")