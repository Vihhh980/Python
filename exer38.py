caractere = input('Digite uma letra (ou "sair" para encerrar): ')

while caractere != "SAIR":
    quantidade = len(caractere)

    if quantidade == 1:
        if caractere == "A" or caractere == "E" or caractere == "I" or caractere == "O" or caractere == "U":
            print("Vogal")
        else:
            print("Consoante")
    else:
        print("Digite apenas 1 caractere!")

    caractere = input('Digite uma letra (ou "sair" para encerrar): ')

print("Programa encerrado.")

