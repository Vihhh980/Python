compra = int(input('Digite o valor da compra: '))

if compra > 500:
    print('Você recebeu 20% de desconto')
    valor = compra * 0.2
    desconto = compra - valor
    print("O valor com desconto:", desconto)

elif compra > 350:
    print('Você recebeu 15% de desconto')
    valor = compra * 0.15
    desconto = compra - valor
    print("O valor com desconto:", desconto)

elif compra > 200:
    print('Você recebeu 10% de desconto')
    valor = compra * 0.1
    desconto = compra - valor
    print("O valor com desconto:", desconto)

else:
    print('SEM DESCONTO')

