
A = []

for i in range(5):#100

    numeros = float(input("Informe um Número: "))
    A.append(numeros)


for i in range(5):#100
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")

