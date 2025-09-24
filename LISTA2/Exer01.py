
telefone = input("Digite o número do telefone (somente números): ")
try:
    if not telefone.isdigit():
      print("O telefone deve conter apenas números.")

    if len(telefone) == 10:
        ddd = telefone[:2]
        parte1 = telefone[2:6]
        parte2 = telefone[6:]
        telefone_formatado = f"({ddd}) {parte1}-{parte2}"

    print("Telefone válido! Formato correto:", telefone_formatado)

except:
  print('ERRO')  