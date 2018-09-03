# 25. Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no fnal a soma da série.



termo = int(input('Insira a quantidade de termos desejada: '))

somaStr = "S = "
s = 0
m = 1
for n in range(1, termo + 1):
    s += n / m
    somaStr += str(n) + "/" + str(m)
    if n != termo:
        somaStr += " + "
    m += 2

print(somaStr)
print('Soma da série: %s' % s)