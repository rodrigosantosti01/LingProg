# Atividade - 6 
# Faça um Programa que peça 2 números inteiros e um número
# real. Calcule e mostre:
# item 1- o produto do dobro do primeiro com metade do segundo .
# item 2- a soma do triplo do primeiro com o terceiro.
# item 3- o terceiro elevado ao cubo.


primeiro_inteiro = 0
segundo_inteiro = 0
numero_real = 0.0
primeiro_inteiro =int(input("Digite um numero inteiro:"))
segundo_inteiro =int(input("Digite outro numero inteiro:"))
numero_real =float(input("Digite um numero real:"))

item_um = ((2*primeiro_inteiro)*(segundo_inteiro/2))
item_dois = ((3*primeiro_inteiro)+numero_real)
item_tres = (numero_real**3)

print ("resultado do item1: %s" %(item_um))
print ("resultado do item2: %s" %(item_dois))
print ("resultado do item3: %s" %(item_tres))
