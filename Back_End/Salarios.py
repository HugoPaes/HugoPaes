"""
Programa que realize a leitura nome e salário
a cada interação deverá perguntar ao usuário se ele deseja continur.

No final, deverá apresentar o número de funcionário lidos e o somatório dos salários.

"""

numerofuncionarios = 0
somasalario = 0.0
while True:
    
    nome = input("Informe o nome: ")
    salario = float(input("Informe o salário:"))
    
    numerofuncionarios = numerofuncionarios + 1
    somasalario = somasalario + salario
    
    opcao = input("Deseja continuar (s/n)? ")
    if opcao.lower()=='n':
        break
print(f"O número de funcinário é {numerofuncionarios}")
print(f"A soma dos salários é {somasalario:.2f}")
    
    
    