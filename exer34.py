num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print('SOMA ou (+)')
print('SUBTRAÇÃO ou (-)')
print('MULTIPLICAÇÃO ou (*)')
print('DIVISÃO ou (/)')
print('Digite "sair" para encerrar.')

escolha = input('Digite a escolha: ')

while escolha != 'sair':
    if escolha == '+' or escolha == 'soma':
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif escolha == '-' or escolha == 'subtracao':
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif escolha == '*' or escolha == 'multiplicacao':
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif escolha == '/' or escolha == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: divisão por zero!")

    else:
        print('Não é válido!')


    escolha = input('Digite a escolha: ')

print('Você saiu.')


