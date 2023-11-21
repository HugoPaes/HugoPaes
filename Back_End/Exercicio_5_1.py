salario = float(input("Informe o salário: "))
cargo = int(input("Informe o código do cargo: "))

nomeCargo = ""
match cargo:
    case 100:
        percentual = 20
        nomeCargo = "Auxiliar Administrativo"
    case 101:
        percentual = 15
        nomeCargo = "Engenheiro"
    case 102:
        percentual = 10
        nomeCargo = "Gerente"
    case _:
        percentual = 0
        nomeCargo = "Cargo Inválido"

reajuste = salario * (percentual/100)

novo_salario = salario + reajuste

print(f"Cargo: {nomeCargo}\nSalário: {salario:.2f}\nReajuste: {reajuste:.2f}\nNovo Salário: {novo_salario:.2f}")