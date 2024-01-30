

for i in range(4):

    frases = input("Informe uma Frase Criativa: ")
    palavras = frases.split()

    apenasLetras = all(palavra.isalpha() for palavra in palavras)#vai verifica se todas frases contém apenas Letras, ás que contém  retornar True
    #e ás que não contém retornar False

    if len(palavras) <= 10 and apenasLetras:

        print(len(palavras),"palavras")
        print("Envio válido")

    else:

        print(len(palavras),"palavras")
        print("Envio inválido")


