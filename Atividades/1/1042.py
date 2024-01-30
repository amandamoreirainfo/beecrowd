
linha = input("Informe os Valores: ")

a, b, c = linha.split()

a = int(a)
b = int(b)
c = int(c)

listaValores = [a, b, c]

for valor in sorted(listaValores):
    print(valor)

print("")

for valor in listaValores:
    print(valor)

