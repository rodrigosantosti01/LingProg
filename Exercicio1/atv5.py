# Atividade - 5 
# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.


gC = 0
gC =int(input("Digite uma temperatura em Celsius:"))
gF = (((gC*9)/5)+32)
print ("Você digitou a temperatura de: %sºC e o seu respectivo valor em Graus Farenheit é: %s" %(gC,"%.2f" %round(gF,2)))