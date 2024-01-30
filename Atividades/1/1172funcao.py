

def substituicao(X):

    X = [0] * 10
    for i in range(10):
        if X[i] <= 0:
            X[i] = 1
    return X


X = []

for i in range(10):
    X[i] = int(input("Informe um Valor: "))

X = substituicao(X)

for i in range(10):
    print(f"X[{i}] = {X[i]}")