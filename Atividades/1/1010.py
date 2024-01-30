
#12 1 5.30
#16 2 5.10

#VALOR A PAGAR: R$ 15.50

linha1 = input("Informe os Valores - 1: ")
linha2 = input("Informe os Valores - 2: ")

codigoPeca1, numeroPeca1, valorUnitarioPeca1 = linha1.split()
codigoPeca2, numeroPeca2, valorUnitarioPeca2 = linha2.split()

codigoPeca1 = int(codigoPeca1)
numeroPeca1 = int(numeroPeca1)
valorUnitarioPeca1 = float(valorUnitarioPeca1)
codigoPeca2 = int(codigoPeca2)
numeroPeca2 = int(numeroPeca2)
valorUnitarioPeca2 = float(valorUnitarioPeca2)

total = (numeroPeca1 * valorUnitarioPeca1) + (numeroPeca2 * valorUnitarioPeca2)

print(f"VALOR A PAGAR: R${total: .2f}")

