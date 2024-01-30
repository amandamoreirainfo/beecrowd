
#3.0 4.0 5.2

#TRIANGULO: 7.800
#CIRCULO: 84.949
#TRAPEZIO: 18.200
#QUADRADO: 16.000
#RETANGULO: 12.000

linha = input("Informe os Valores: ")

A, B, C = linha.split()

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

areaTriangulo = 1/2 * A * C
areaCirculo = pi*C**2
areaTrapezio = (A+B)*C/2
areaQuadrado = B**2
areaRetangulo = A*B


print(f"TRIANGULO:{areaTriangulo: .3f}")
print(f"CIRCULO:{areaCirculo: .3f}")
print(f"TRAPEZIO:{areaTrapezio: .3f}")
print(f"QUADRADO:{areaQuadrado: .3f}")
print(f"RETANGULO:{areaRetangulo: .3f}")


