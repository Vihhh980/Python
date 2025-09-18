Idade = int(input('Digite uma idade: '))

if Idade < 8:
  print('Grátis')
elif Idade > 8 and Idade< 18:
  print("O valor da passagem é 70R$")
else:
    print("O valor da passagem é 140$")