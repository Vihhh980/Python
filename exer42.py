X = float(input('Digite um número: '))
Y = float(input('Digite o segundo número: '))

if X > 0 and Y > 0:
  print("Quadrante I")

elif X < 0 and Y > 0:
  print('Quadrante II')


elif X < 0 and Y < 0:
  print('Quadrante IIi')

else:
  print("Quadrante IV")