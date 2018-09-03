
# 13. Faça um programa que peça uma nota, entre zero e dez. Mostre
# uma mensagem caso o valor seja inválido e continue pedindo até
# que o usuário informe um valor válido.


num = int(input("Digite uma nota entre zero e dez: "))
while num < 0 or num > 10:
    print("Valor inválido.")
    num = int(input("Digite uma nota entre zero e dez: "))
else:
    print("Valor válido.")