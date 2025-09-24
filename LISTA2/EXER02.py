Quantidade = int(input('Digite a quantidade de notas'))
soma = 0
for i in range(Quantidade):
  i = i + 1
  nota = float(input("Digite a sua nota "))
  if nota>10 or nota <0:
    print('Digite um número válido')
    break
  soma += nota
else:
  media = soma/i
  if media >= 6:
    print('Aprovado')
  elif media < 6:
    print("Reprovado")
