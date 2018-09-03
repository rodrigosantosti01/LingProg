# 20. Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120




fatorial = int(input("Fatorial de: "))
for i in range(1, fatorial):
    fatorial = fatorial * i
print(fatorial)