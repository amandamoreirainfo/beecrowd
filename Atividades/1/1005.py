
#5.0
#7.1

#MEDIA = 6.43182

A = float(input("Informe a Nota do Aluno - A: "))
B = float(input("Informe a Nota do Aluno - B: "))

pesoA = 3.5
pesoB = 7.5

MEDIA = ( pesoA * A  + pesoB * B) / (pesoA + pesoB)

print(f"MEDIA ={MEDIA: .5f}")
