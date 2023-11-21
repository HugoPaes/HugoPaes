matriz = []

matriz.append(['luis', 'lrpfeliciano.com', '1020-2020'])
matriz.append(['renato', 'renato@teste.com', '2123-2020'])

for elemento in matriz:
    for elem in elemento:
        print(elem)
        
for elemento in matriz:
    saida = ''
    saida = saida + elem + "\t"
    
    print(saida)