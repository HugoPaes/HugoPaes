agenda = {}

agenda['nome'] = input("informe o nome: ")
agenda['email'] = input("Informe o email: ")
agenda['telefone'] = input("informe o telefone: ")

agenda = []
agenda.append('Cadastro')

for contato in agenda:
    print(contato['nome'])
    
