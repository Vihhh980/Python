estoque = []

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto (CREATE)")
    print("2 - Listar produtos (READ)")
    print("3 - Atualizar produto (UPDATE)")
    print("4 - Remover produto (DELETE)")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        estoque.append((codigo, nome, quantidade))
        print("Produto cadastrado com sucesso!")
    elif opcao == "2":
        if not estoque:
            print("Estoque vazio.")
        else:
            print("Produtos em estoquE")
            for item in estoque:
                print(f"Código: {item[0]} | Nome: {item[1]} | Quantidade: {item[2]}")
    elif opcao == "3":
        codigo = input("Digite o código do produto a atualizar: ")
        encontrado = False
        for i in range(len(estoque)):
            if estoque[i][0] == codigo:
                nome = input("Novo nome: ")
                quantidade = int(input("Nova quantidade: "))
                estoque[i] = (codigo, nome, quantidade) 
                encontrado = True
                print("Produto atualizado!")
                break
        if not encontrado:
            print("Produto não encontrado.")
    elif opcao == "4":
        codigo = input("Digite o código do produto a remover: ")
        estoque = [item for item in estoque if item[0] != codigo]
        print("Produto removido, se existia.")
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
