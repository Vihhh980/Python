listaPessoas = []

while True:
    print("MENU")
    print("1 - Cadastrar")
    print("2 - Ler")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Código da pessoa: ")
        nome = input("Nome da pessoa: ")
        listaPessoas.append((codigo, nome))
        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if not listaPessoas:
            print("Ninguém cadastrado.")
        else:
            print("\nPessoas cadastradas:")
            for item in listaPessoas:
                print(f"Código: {item[0]} | Nome: {item[1]}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
