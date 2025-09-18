dia = int(input('Digite um dia'))
mes = int(input("Digite a data do mês"))
ano = int(input("Digite o dia do ano"))

if dia > 1 and dia < 31 and mes> 1 and mes < 12 and mes< 2025:
  print('Permitido')
else:
   print('Negado')