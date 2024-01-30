#5.0
#6.0
#7.0

#MEDIA = 6.3

A = float(input("Informe o Nota do Aluno - A: "))
B = float(input("Informe o Nota do Aluno - B: "))
C = float(input("Informe o Nota do Aluno - C: "))

pesoA = 2
pesoB = 3
pesoC = 5

MEDIA = (pesoA * A + pesoB * B + pesoC * C) / (pesoA + pesoB + pesoC)

print(f"MEDIA ={MEDIA: .1f}")