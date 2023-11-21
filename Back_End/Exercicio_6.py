soma = 0
media = 0

for contador in range (10):
    numero = int(input("informe numero: "))
    soma += numero

media = soma / 10

print(f'A soma é {soma}\nA media é {media:.2f}')