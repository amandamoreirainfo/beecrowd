#400

#1 ano(s)
#1 mes(es)
#5 dia(s)

idadeDias = int(input("Informe a Idade da Pessoa: "))

ano = idadeDias // 365
meses = (idadeDias % 365) // 30
dias = (idadeDias % 365) % 30

print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
