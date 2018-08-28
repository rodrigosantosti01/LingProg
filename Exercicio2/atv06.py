#Atividade - 6 
# Escreva um programa que lê̂ duas notas de vários alunos e
# armazena tais notas em um dicionário, onde a chave é o nome do
# aluno. A entrada de dados deve terminar quando for lida uma string
# vazia como nome. Escreva uma função que retorna a média do
# aluno, dado seu nome.


dict = {}
nota = 0.0
aluno = " "
while aluno != "":
    aluno = str(input("Informe o nome do aluno ou Aperte enter para sair: "))
    if (aluno != ""):
        nota1 = float(input("Informe a primeira nota do aluno %s: " %(aluno)))
        nota2 = float(input("Informe a segunda nota do aluno %s: " %(aluno)))
        dict[aluno] = {'notas':[nota1, nota2]}

for chave, valor in dict.items():
    media = (sum(valor['notas']) / len(valor['notas']))
    print("A média do aluno %s é: %s" %(chave, media))