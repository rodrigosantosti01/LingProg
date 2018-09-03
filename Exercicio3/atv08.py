# 8. Faça um Programa que peça os 3 lados de um triângulo. O
# programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois
# lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;



a = float(input("Digite o primeiro lado do triangulo: "))
b = float(input("Digite o segundo lado do triangulo: "))
c = float(input("Digite o terceiro lado do triangulo: "))

if a < b + c and  b < a + c and c < a + b:
    print('Os valores podem ser um triângulo.')
    if a == b == c:
        print('Os valoresa formam um triângulo equilátero.')
    elif a == b or a == c or c == b:
        print('Os valores formam um triângulo isósceles.')
    else:
        print('Os valores formam um triângulo escaleno.')
else:
    print('Os valores não podem ser um triângulo'). 