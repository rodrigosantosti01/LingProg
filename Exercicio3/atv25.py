#25.  Faça um programa que receba o valor de uma dívida e mostre
# uma tabela com os seguintes dados: 
# valor da dívida, valor dos juros,
# quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
# 1 0
# 3 10
# 6 15
# 9 20
# 12 25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
# R$ 1.000,00 0 1 R$ 1.000,00
# R$ 1.100,00 100 3 R$ 366,00
# R$ 1.150,00 150 6 R$ 191,67



dividaInicial = float(input("Insira o valor da dívida: "))
print("Dívida \t Valor Juros \t Qtde Parcelas \t Valor da Parcela")
for i in range(0, 5):
    if i == 0:
        juros = 0
    elif i == 1:
        juros = 10
    else:
        juros += 5
    valorJuros = dividaInicial * (juros / 100)
    divida = dividaInicial + valorJuros
    if i == 0:
        qtdeParc = 1
    else:
        qtdeParc = i * 3
    if qtdeParc != 0:
        valorParcela = divida / qtdeParc
    else:
        valorParcela = divida
    print(f"R$ {divida} \t {valorJuros} \t {qtdeParc} \t R$ %.2f"%(valorParcela))