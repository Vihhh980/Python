peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))
Imc = peso/(altura*altura)
if Imc < 16.0:
  print('Magreza')
elif Imc > 16 and Imc < 17:
  print('Magreza Moderada')

elif Imc > 17 and Imc < 18.5:
  print('magreza leve')


elif Imc > 18.5 and Imc < 25:
  print('Saudável')


elif Imc > 25 and Imc < 30:
  print('Sobrepeso')


elif Imc > 30 and Imc < 35:
  print('Obsidade Grau I')

elif Imc > 35 and Imc < 40:
  print('Obsidade Grau II')
else:
  print('Obsidade Grau III')

