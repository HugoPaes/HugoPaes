from funcoes import incluir, pesquisar, listar


def menu():
    print("1 - Cadastro")
    print("2 - Pesquisar Nome")
    print("3 - Listar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("9 - Sair")


agenda = []
while True:
    menu()
    opcao = int(input("Informe a opção: "))

    if opcao == 1:
        incluir(agenda)

    elif opcao == 2:
        nomeBusca = input("Infomre o nome para busca: ")
        indice = pesquisar(agenda, nomeBusca)
        if indice != -1:
            print(
                f"""{agenda[indice]['nome']} 
                   - {agenda[indice]['email']} - 
                   {agenda[indice]['telefonme']}"""
            )
        else:
            print("Contato não encontrado")
    elif opcao == 3:
        listar(agenda)
    elif opcao == 4:
        nomeBusca = input("Infomre o nome para busca: ")
        posicao = pesquisar(agenda, nomeBusca)
        

        if posicao != -1:
            agenda[posicao]["nome"] = input("Informe o nome:")
            agenda[posicao]["email"] = input("Informe o email:")
            agenda[posicao]["telefone"] = input("Informe o telefone:")

    elif opcao == 5:
        nomeBusca = input("Infomre o nome para busca: ")
        posicao = pesquisar(agenda, nomeBusca)
       
        if posicao != -1:
            agenda.pop(posicao)

    elif opcao == 9:
        break
    else:
        print("Opção Inválida.")
