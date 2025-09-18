print("Bem-vindo(a) ao jogo de adivinhação")
print("Você terá 5 chances e 5 dicas.")

palavra = "PYTHON"
vida = 0
while vida < 5:
    letra = input("Digite a palavra:")

    if letra == palavra:
        print("Você ganhou!")
        break
    else:
        vida = vida + 1
        if vida == 1:
            print("É uma linguagem de programação")

        elif vida == 2:
            print("É uma linguagem de alto nível")

        elif vida == 3:
            print("É orientada a objetos")

        elif vida == 4:
            print("Sua primeira letr começa com P")

        elif vida == 5:
            print("É multipropósito e multiplataforma")

if letra != palavra:
    print("Você perdeu! A palavra era:", palavra)

