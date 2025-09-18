ano = int(input('Digite o ano'))
if ano % 4 == 0:
  print('Bissexto')
elif ano%400 == 0:
  print(' Bissexto')
else:
    print('Não é Bissexto')
