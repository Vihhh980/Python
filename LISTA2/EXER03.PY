print('Calculadora de Bases Numéricas')
print('Escolha entre as opções: binário, octal, hexadecimal')
escolha1 = input('Digite a sua escolha: ')
Numero = int(input("Digite um número: "))
if escolha1 == 'binário':
    binario = ""
    numero_temp = Numero
    while numero_temp > 0:
        resto = numero_temp % 2
        binario = str(resto) + binario
        numero_temp = numero_temp // 2
    print(f"O valor {Numero} em binário é: {binario}")
elif escolha1 == 'octal':
    octal = ""
    numero_temp = Numero
    while numero_temp > 0:
        resto = numero_temp % 8
        octal = str(resto) + octal
        numero_temp = numero_temp // 8
    print(f"O valor {Numero} em octal é: {octal}")

elif escolha1 == 'hexadecimal':
    hexa = ""
    numero_temp = Numero
    while numero_temp > 0:
        resto = numero_temp % 16
        if resto < 10:
            hexa = str(resto) + hexa
        else:
            hexa = chr(55 + resto) + hexa
        numero_temp = numero_temp // 16
    print(f"O valor {Numero} em hexadecimal é: {hexa}")
else:
    print('Escolha Inválida')



