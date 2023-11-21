print('{:=^40}'.format(' LOJAS AMERICANAS '))
preço = float(input('Preço das compras: R$'))
print('''Formas de Pagamento
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista no cartão
      [ 3 ]2x no cartão
      [ 4 ]3x ou mais no cartão''')
opção = int(input('Qual é a Opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2 
    print('Sua compra será parcela em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção invalida de pagamento. tente Novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))