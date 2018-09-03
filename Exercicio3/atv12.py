# 12. Uma fruteira está vendendo frutas com a seguinte tabela de
# preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
# sobre este total. Escreva um algoritmo para ler a quantidade (em
# Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
# escreva o valor a ser pago pelo cliente.



preco = 0
kgMorg = float(input("Insira a quantidade em kg de morangos: "))
kgMaca = float(input("Insira a quantidade em kg de maçãs: "))

if kgMorg < 5:
    preco += kgMorg * 2.50
else:
    preco += kgMorg * 2.20
    
if kgMaca < 5:
    preco += kgMaca * 1.80
else:
    preco += kgMaca * 1.50
    
if preco > 25.00:
    preco *= 0.90

print('Valor a ser pago: ', preco)