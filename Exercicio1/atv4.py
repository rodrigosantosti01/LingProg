# Atividade - 4
# Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32)/9).

gF = 0
gF =int(input("Digite uma temperatura em Farenheit:"))
gC= (5*(gF-32)/9)
print ("Você digitou a temperatura de: %sºF e o seu respectivo valor em Graus Celsius é:  %s" %(gF,"%.2f" %round(gC,2)))