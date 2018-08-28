import sys


agenda = {}

def incluirNovoNome(nome="", telefones=[]):
    agenda[nome] = telefones   
    return agenda


def incluirTelefone(nome = "",  telefone= ""):
    if nome not in agenda:
        deseja_inserir = int(input("nome não existe na agenda, deseja inserir?: \n 0-não ou 1-sim  "))
        if deseja_inserir:
            incluirNovoNome(nome)
        else: 
            return
    
    agenda[nome].append(telefone)    
    
    return agenda


def excluirNome(nome=""):
    agenda.pop(nome)
    return agenda


def excluirTelefone(nome,telefone):
    if nome not in agenda:
        print("nome nao existe na agenda")
        return
    else:
        if telefone in agenda[nome]:
            agenda[nome].pop(agenda[nome].index(telefone))
        if not len(agenda[nome]):
            excluirNome(nome)
    return agenda


def consultarTelefone(nome):
    agenda_bonita = "{} : {}".format(nome, [ telefone for telefone in agenda[nome]])
    return agenda_bonita

if __name__ == '__main__':
    opcao = -1
    while opcao != 0:
        opcao = int(input("tecle 0 - para sair  \n tecle 1 - para inserir o nome \n tecle 2 - para inserir telefones  \ntecle 3 - para remover \ntecle 4 - para remover o telefone \n tecle 5 - para consultar telefones"))
        if opcao == 0:
            sys.exit(0)
        elif opcao ==1:
            nome = input("Digite um nome: ")
            incluirNovoNome(nome, [])
        elif opcao ==2:
            nome = input("Digite o nome que existe na agenda: ")
            telefone = input("Digite telefone: ")
            incluirTelefone(nome,telefone)
        elif opcao ==3:
            nome = input("Digite o nome da agenda a ser removido: ")
            excluirNome(nome)
        elif opcao ==4:
            nome = input("Digite um nome para excluir o telefone: ")
            telefone = input("Digite o telefone a ser removido")
            excluirTelefone(nome,telefone)
        elif opcao ==5:
            nome = input("Digite um nome para consultar os telefones ")
            consultarTelefone(nome)
        else:
            print ("Opcao invalida:")

        print (agenda)