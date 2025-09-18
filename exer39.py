CadastroEmail = input('Digite o seu email')
Senha = int (input('Digite a sua senha'))

EmailLogin = input('Digite o seu email')
SenhaLogin = int (input('Digite a sua senha'))

if EmailLogin == CadastroEmail and SenhaLogin == Senha:
  print('Aprovado')

else:
  print("Acesso Negado")

