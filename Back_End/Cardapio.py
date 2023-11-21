while True:
    codigo = int(input("Informe o Código: "))
    quantidade = int(input("Informe a quantidade: "))
    
    if codigo == 100:
        preco = 1.2
    elif codigo == 101:
        preco = 1.3
    elif codigo == 102:
        preco = 1.5
    elif codigo == 103:
        preco = 1.2
    elif codigo ==104:
        preco = 1.3
    elif codigo == 105:
        preco = 1.0
    else: 
        preco = 0
        print("codigo Inválido.")
    
    valor = valor + (preco * quantidade)
    opcao = input("Deseja continuar (s/n)? ") 
    if opcao.lower() == 'n':
        break
print(f"O é valor{valor}")
print(f"A soma dos salários é {somasalario:.2f}")
