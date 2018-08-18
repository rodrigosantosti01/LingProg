# Atividade - 12
# Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
# extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.
# Obs.: Não use desvio condicional nem loops.

import datetime

date_entrada = input('Coloque sua data de nascimento DD/MM/AAAA: ')
print("Data de Nascimento: %s"  %(date_entrada))
ano,mes,dia = map(int, date_entrada.split('/'))
date1 = datetime.date(dia, mes, ano)
d = date1.strftime('%d/%B/%Y')
ano, mes,dia = map(str, d.split('/'))
print ("Você nasceu em %s de %s de %s" %(ano, mes,dia))


