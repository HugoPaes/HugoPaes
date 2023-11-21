vetor = []
# Entrada
while True:
    numero = int(input("Informe o Número: "))
    if numero == 0:
        break
    vetor.append(numero)
    
#Processamento
soma = 0
for elemento in vetor:
    soma = soma + elemento
    
#saida

print(f"A soma de todos os elementos é {soma}")
media = soma / len(vetor) 
print(f"A média é {media}")
