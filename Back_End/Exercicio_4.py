# Definir categoria do nadador
#Pega a idade do nadador
idade = int(input("Informe a Idade: "))
# Ifs para verificar entre qual faixa de idade se encontra o nadador
if idade >= 5 and idade <= 7:
    print('infantil A')

elif 8 >= idade and idade <= 10:
    print('infantil B')
    
elif 11 >= idade and idade <= 13:
    print('Juvenil A')
    
elif 14 >= idade and idade <= 17:
    print('juvenil B')
    
else:
    print ('Adulto acima de 18')