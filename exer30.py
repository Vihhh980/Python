Nota1 = float (input('Digite a nota 1'))
Nota2 = float (input('Digite a nota 2'))
Nota3 = float (input('Digite a nota 3'))
Nota4 = float (input('Digite a nota 4'))
media = (Nota1 + Nota2 + Nota3 + Nota4)/4
print(media)
if media <6 and media<10:
  print('Aprovado')
elif media > 5 and media <4:
  print('Retido')
else:
  print('Reprovado')