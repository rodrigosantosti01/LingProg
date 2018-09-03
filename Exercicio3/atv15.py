# 15. Faça um programa que leia 5 números e informe o maior
# número.




maior  =  int(input("Digite o 1º número:"))
for num in range(2,6):
    x = int(input(f"Digite o {num}º número: "))
    if x > maior:
        maior = x
print("Maior:", maior)