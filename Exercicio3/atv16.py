# 16. Faça um programa que leia 5 números e informe a soma e a
# média dos números.



soma = 0
for num in range(1,6):
    soma += int(input(f"Digite o {num}º número: "))
print("Soma:", soma)
print("Media:", soma / 5)