
valor = 5
def cafe(f):
    def decorador(adc):
        return f(adc)
    return decorador 

@cafe
def cafe_funcao(adc):
    return adc


entrada = int(input("Menu: \n 1-Para Palitos de chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
while (entrada != 0):
    if (entrada ==1):
        print("chocolate")
        valor += cafe_funcao(0.50)
    if(entrada == 2):
        print("espuma de leite")
        valor += cafe_funcao(0.20)
    if(entrada == 3):
        print("Caramelo")
        valor += cafe_funcao(0.10)
    if (entrada ==4):
        print("Canela")
        valor  += cafe_funcao(0.30)
    entrada = int(input("Digite: \n 1-Para chocolate \n 2-Para espuma de leite \n 3-Para caramelo \n 4-Para Canela \n 0-Sair \n"))
print(valor)
