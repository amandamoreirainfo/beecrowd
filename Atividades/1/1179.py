pares = []
impares = []

for i in range(15):
    N = int(input("Informe um número: "))

    if N % 2 == 0:
        pares.append(N)
        if len(pares) == 5:
            for a in range(5):
                print(f"par[{a}] = {pares[a]}")
            pares.clear()
    else:
        impares.append(N)
        if len(impares) == 5:
            for  b in range(5):
                print(f"impar[{b}] = {impares[b]}")
            impares.clear()



for z in range(len(impares)):
    print(f"impar[{z}] = {impares[z]}")


for y in range(len(impares)):
    print(f"par[{y}] = {pares[y]}")
