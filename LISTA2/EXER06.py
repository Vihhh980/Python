lista = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

ListaJogadas = ["A1","A2","A3",
                "B1","B2","B3",
                "C1","C2","C3"]

print("|A1|A2|A3|\n|B1|B2|B3|\n|C1|C2|C3|")
jogada = input("Jogador X, digite a sua jogada: ")

if jogada not in ListaJogadas:
    print("Jogada inválida!")
else:
  if jogada[0] == 'A':
    linha = 0
  elif jogada[0] == 'B':
    linha = 1
  elif jogada[0] =='C':
    linha = 2
  if jogada[1] == "1":
        coluna = 0
  elif jogada[1] == "2":
        coluna = 1
  elif jogada[1] == "3":
        coluna = 2
  lista[linha][coluna] = "X"
for l in lista:
    print(l)