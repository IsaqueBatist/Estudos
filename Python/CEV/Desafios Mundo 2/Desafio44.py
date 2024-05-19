'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição
de pagamento
Á vista: dinheiro/cheque: 10% de desconto
À vista: cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''
print('{:=^10}'.format(' LOJAS ISAQUE '))
valor = float(input('Qual o valor do porduto?'))
print('''FORMAS DE PAGAMENTO
      [1] á vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção?'))
if opcao == 1:
  preco = valor - valor*0,1
  print('Sua compra com 10% de desconte é de: R${}' .format(valor))
elif opcao == 2:
  preco = valor - valor*0.5
  print('Sua compra À vista no cartão com desconto de 5% é de R${}' .format(valor))
elif opcao == 3:
  preco = valor
  print('Sua compra parcelada em 2x não terá alterações R${}' .format(preco))
elif opcao == 4:
  parcela = int(input('Quantas parcelas?'))
  valorparcela = valor/parcela
  valorf = valor + valor*0.2
  print('Sua compra serpa parcelada em {}x de R${} COM JUROS sua compra de R${} vai custar R${} no final.' .format(parcela, valorparcela, valor, valorf))
else:
  print('Opção INVÁLIDA')