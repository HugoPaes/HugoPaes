def incluir(vetor):
    pessoa = {}
    pessoa["nome"] = input("informe o nome: ")
    pessoa["email"] = input("Informe o email: ")
    pessoa["telefone"] = input("informe o telefone: ")
    
    vetor.append(pessoa)
    
def pesquisar(vetor, nomeBusca):
        posicao = -1
        encontrado = False
        for elemento in vetor:
            posicao = posicao + 1
            if elemento['nome'].lower() == nomeBusca.lower():
                encontrado = True
                break
        if encontrado:
            return posicao
    
        else:
            return -1
        
def listar(vetor):
    for elemento in vetor:
        print(f"""{elemento['nome']}\t
        {elemento['email']}
        \t{elemento['telefone']}""")
        
def excluir(vetor, nomeBusca):
        posicao = -1
        encontrado = False
        for elemento in vetor:
            posicao = posicao + 1
            if elemento['nome'].lower() == nomeBusca.lower():
                encontrado = True
                break
        if encontrado:
            return posicao
    
        else:
            return -1
        