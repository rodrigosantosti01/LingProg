# Atividade - 7 
# Uma pista de Kart permite 10 voltas para cada um de 6
# corredores. Escreva um programa que leia todos os tempos em
# segundos e os guarde em um dicionário, onde a chave é o nome do
# corredor. Ao fnal diga de quem foi a melhor volta da prova e em
# que volta; e ainda a classifcação fnal em ordem (1o o campeão). O
# campeão é o que tem a menor média de tempos.



import  sys

corredor_menor_tempo = sys.maxsize
corredor_menor_tempo_nome = ""
volta = ""
corrida_kart = {}
tempo_final = {}

corredor1 = {'Jorge':{'Voltas':{'Volta 1':301, 'Volta 2':290, 'Volta 3':288, 'Volta 4':291, 'Volta 5':292, 'Volta 6':287, 'Volta 7':285, 'Volta 8':300, 'Volta 9':302, 'Volta 10':309}}} 
corredor2 = {'Leonardo':{'Voltas':{'Volta 1':290, 'Volta 2':212, 'Volta 3':205, 'Volta 4':254, 'Volta 5':248, 'Volta 6':278, 'Volta 7':219, 'Volta 8':240, 'Volta 9':233, 'Volta 10':252}}}
corredor3 = {'Rodrigo':{'Voltas':{'Volta 1':277, 'Volta 2':197, 'Volta 3':209, 'Volta 4':195, 'Volta 5':206, 'Volta 6':209, 'Volta 7':270, 'Volta 8':258, 'Volta 9':278, 'Volta 10':297}}}
corredor4 = {'Guilherme':{'Voltas':{'Volta 1':190, 'Volta 2':288, 'Volta 3':239, 'Volta 4':242, 'Volta 5':228, 'Volta 6':289, 'Volta 7':261, 'Volta 8':288, 'Volta 9':295, 'Volta 10':279}}}
corredor5 = {'Renan':{'Voltas':{'Volta 1':300, 'Volta 2':219, 'Volta 3':224, 'Volta 4':266, 'Volta 5':222, 'Volta 6':239, 'Volta 7':253, 'Volta 8':300, 'Volta 9':252, 'Volta 10':266}}}
corredor6 = {'Fabricio':{'Voltas':{'Volta 1':223, 'Volta 2':364, 'Volta 3':295, 'Volta 4':245, 'Volta 5':212, 'Volta 6':282, 'Volta 7':238, 'Volta 8':225, 'Volta 9':266, 'Volta 10':227}}}
corrida_kart.update(corredor1)
corrida_kart.update(corredor2)
corrida_kart.update(corredor3)
corrida_kart.update(corredor4)
corrida_kart.update(corredor5)
corrida_kart.update(corredor6)

for chave, valor in corrida_kart.items():
    if corredor_menor_tempo > min(valor['Voltas'].values()):
        corredor_menor_tempo = min(valor['Voltas'].values())
        corredor_menor_tempo_nome = chave
        volta = min(valor['Voltas'], key=valor['Voltas'].get)
        
def calcula_media(valores, tamanho):
    return (sum(valores) / tamanho)
    
for chave, valor in corrida_kart.items():
    tempoMedio = calcula_media(valor['Voltas'].values(), len(valor['Voltas'].values()))
    tempo_final.update({chave:tempoMedio})

classificacao_final = sorted(tempo_final.items(), key=lambda elem: elem[1])

print("Melhor volta da corrida pelo corredor: %s na %s em %ss" %(corredor_menor_tempo_nome, volta, corredor_menor_tempo))
print("Classificação final:")
i = 1
for chave, valor in classificacao_final:
    print("%so Lugar: %s com tempo médio de %ss." %(i, chave, valor))
    i += 1

