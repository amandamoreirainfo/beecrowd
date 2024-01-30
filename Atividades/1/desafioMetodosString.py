

namesCadastrados = []

for i in range(4):

    name = input("Informe os Nomes Cadastrados: ")

    #Remover os numeros do nome
    removeNumeros = "".join(caracter for caracter in name if not caracter.isdigit())

    partes = removeNumeros.split() #dividir o nome em partes usando espaços como delimitador

    nameCapitalize = [parte.capitalize() for parte in partes] #transformar nome e sobrenome com a primeira letra inicial sendo maiscula

    nameCapitalize = " ".join(nameCapitalize)#Juntar as partes para formar o nome e sobrenome, pq tive separar por partes para fazer ás formatações.

    namesCadastrados.append(nameCapitalize)

print(namesCadastrados)