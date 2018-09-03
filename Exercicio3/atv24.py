# 24. Foi feita uma estatística em cinco cidades brasileiras para
# coletar dados sobre acidentes de trânsito. Foram obtidos os
# seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Desejase
# saber:
# - Qual o maior e menor índice de acidentes de transito e a que
# cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de
# 2.000 veículos de passeio.



cidades = {
    #cod #veiculos #acidentes
    "cidade0": [6753, 12],
    "cidade1": [7503, 23],
    "cidade2": [607, 3],
    "cidade3": [450, 2],
    "cidade4": [12045, 47]
}

menorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
maiorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
somaVeiculos = 0
somaAcidentes = 0
contCidades = 0
for cod in cidades:
    somaVeiculos += cidades[cod][0]
    if cidades[cod][0] < 2000:
        somaAcidentes += cidades[cod][1]
        contCidades += 1
    if cidades[cod][1] > maiorIndice[0]:
        maiorIndice[0] = cidades[cod][1]
        maiorIndice[1] = cod
    if cidades[cod][1] < menorIndice[0]:
        menorIndice[0] = cidades[cod][1]
        menorIndice[1] = cod
        
    
mediaVeiculos = somaVeiculos / len(cidades.keys())
mediaAcidentes = somaAcidentes / contCidades

print("Maior índice e a cidade: ", maiorIndice)
print("Menor índice e a cidade: ", menorIndice)
print("Média de veículos nas cinco cidades juntas: ", mediaVeiculos)
print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: ", mediaAcidentes)