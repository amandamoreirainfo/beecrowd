
def multiplos(A,B):

    A = int(A)
    B = int(B)

    if A % B  == 0 or B % A == 0:
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"


linha = input("Informe os Valores: ")
A,B = linha.split()
print(multiplos(A,B))