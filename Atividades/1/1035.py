
linha = input("Informe os Valores: ")

A, B, C, D = linha.split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and C + D > A + B:
    if A % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores não aceitos")
else:
    print("Valores não aceitos")
