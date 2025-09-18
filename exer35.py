Lado1 = int(input("Digite o primeiro lado"))
Lado2 = int(input("Digite o segundo lado"))
Lado3 = int(input("Digite o primeiro lado"))

if Lado1 == Lado2 and Lado2 == Lado3:
  print('Equilátero')
elif Lado1 == Lado2 or Lado3 == Lado2 or Lado1 == Lado3:
  print('Isóceles')
else:
  print('Escaleno')
