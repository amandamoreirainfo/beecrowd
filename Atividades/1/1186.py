

operacao = input("Digite S para soma ou M para média: ")
M = []

for i in range(12):

    linha = []
    for j in range(12):

        linha.append(float(input("Informe um número: ")))
    M.append(linha)

soma = 0
elementos = 0

for i in range(12):
    for j in range(12):
        if j < 11 - 1:
            soma += M[i][j]
            elementos += 1


if operacao == "S":
    print(f"{soma:.1f}")
elif operacao == "M":
    media = soma / elementos
    print(f"{media:.1f}")
