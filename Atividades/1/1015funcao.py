import math

def distancia(x1, y1, x2, y2):

    DISTANCIA = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return DISTANCIA


linha1 = input("Informe os Valores do Linha 1: ")
linha2 = input("Informe os Valors do Linha 2: ")

x1, y1 = linha1.split()
x2, y2 = linha2.split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

DISTANCIA = distancia(x1, y1, x2, y2)
print(f"{DISTANCIA:.4f}")
