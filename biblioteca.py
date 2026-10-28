
livros = [ ]

def cadastrar_livro():
    quantidade = int(input("Quantos livros você deseja cadastrar? "))
    print()

    if quantidade == 1:
        nome_livro = input("Nome do livro: ").lower()
        livro = {
            "nome": nome_livro,
            "disponivel": True
            }
        
        livros.append(livro)
        print( )            
        print("1 livro cadastrado com sucesso!")
        

    elif quantidade >= 2:
        for i in range(quantidade):
            nome_livro = input("Nome do livro: ").lower()
            livro = {
                "nome": nome_livro,
                "disponivel": True
                }

            livros.append(livro)
        print( )
        print(quantidade, "livros cadastrados com sucesso!")

    else:
        print("Opção inválida.")

def listar_livros():
    if not livros:
        print("Você precisa cadastrar um livro!")

    else:
        print("Lista de livros:")
        print( )
        
        for livro in livros:
            if livro["disponivel"]:
                print("-", livro["nome"], "- Disponível")
            else:
                print("-", livro["nome"], "- Emprestado")

def buscar_livro():
    if not livros:
        print("Você precisa cadastrar um livro!")

    else:
        livro_busca = input("Qual livro você deseja buscar? ").lower()
        encontrado = False

        for livro in livros:
            if livro_busca == livro["nome"]:
                print( )
                print("O livro", livro_busca, "está na lista!")
                encontrado = True
                break

        if not encontrado:
            print( )
            print("O livro", livro_busca, "não está na lista!")

def emprestar_livro():
    if not livros:
        print("Você precisa cadastrar um livro!")

    else:
        livro_emprestado = input("Qual livro você deseja emprestar? ").lower()
        encontrado = False

        for livro in livros:
            if livro_emprestado == livro["nome"]:
                encontrado = True

                if livro["disponivel"]:
                    livro["disponivel"] = False
                    print( )
                    print(livro_emprestado, "emprestado com sucesso!")

                else:
                    print( )
                    print("Este livro já foi emprestado!")

                break


        if not encontrado:
            print( )
            print("Livro não encontrado.")

def devolver_livro():
    if not livros:
        print("Você precisa cadastrar um livro!")

    else:
        livro_devolvido = input("Qual livro você deseja devolver? ").lower()
        encontrado = False

        for livro in livros:
            if livro_devolvido == livro["nome"]:
                encontrado = True

                if not livro["disponivel"]:
                    livro["disponivel"] = True
                    print( )
                    print(livro_devolvido, "devolvido com sucesso!")

                else:
                    print( )
                    print("Este livro já está na prateleira!")

                break

        if not encontrado:
            print( )
            print("Livro não encontrado.")



while True:
    print( )
    print("=== BIBLIOTECA! ===")
    print( )
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Empréstimo de livro")
    print("5 - Devolução de livro")
    print("6 - Sair")
    print( )

    opcao = input("Qual opção você deseja? ")
    print( )


    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        buscar_livro()

    elif opcao == "4":
        emprestar_livro()

    elif opcao == "5":
        devolver_livro()

    elif opcao == "6":
        print("Saindo da biblioteca. Até mais!")
        break

    else:
        print("Opção indisponível.")