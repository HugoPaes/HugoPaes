pessoa1 = {}

pessoa1['nome'] = "Renato"
pessoa1['email'] = 'renato@teste.com'
pessoa1['telefone'] = '2323-2424'

pessoa2 = {}
pessoa2['telefone'] = '2323-2425'
pessoa2['email'] = 'luiza@teste.com'
pessoa2['nome'] = 'luiza'

pessoa3 = {}

pessoa3['nome'] = input("informe o nome: ")
pessoa3['email'] = input("Informe o email: ")
pessoa3['telefone'] = input("informe o telefone: ")

agenda = []
agenda.append(pessoa1)
agenda.append(pessoa2)
agenda.append(pessoa3)

for contato in agenda:
    print(contato['nome', 'email', 'telefone'])
    