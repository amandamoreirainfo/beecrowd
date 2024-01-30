#400

#1 ano(s)
#1 mes(es)
#5 dia(s)

def idadeEmDias(idadeDias):

    ano = idadeDias // 365
    meses = (idadeDias % 365) // 30
    dias = (idadeDias % 365) % 30
    return ano, meses, dias


idadeDias = int(input("Informe a Idade da Pessoa: "))

ano, meses, dias = idadeEmDias(idadeDias)

print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
