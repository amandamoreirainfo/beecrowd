

X = [0] * 10

for i in range(10):

    X[i] = int(input("Informe um Valor: "))


for i in range(10):
    
    if X[i] <= 0:
        X[i] = 1

for i in range(10):

    print(f"X[{i}] = {X[i]}")