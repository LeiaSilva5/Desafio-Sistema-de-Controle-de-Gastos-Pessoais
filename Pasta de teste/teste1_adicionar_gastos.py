# Entender como adicionar os gastos 

'''
Adicionar gastos :
vamos entender como funcionaria essa função
Tipos de informação
- Descrição do gasto
- Valor do gasto
- Categoria
pra isso vou precisar de funções input() e dicionarios para armazenar a informação

'''
#Primeiro teste
# gastos = []
# descricao = input('Digite uma descrição: ')
# valor = input('Digite o valor do gasto: ')
# categoria = input('Defina uma categoria : ')
# valor = float(valor)
# info = {
#     'Descricao': descricao,
#     'Valor': valor,
#     'Categoria':categoria
# }

# gastos.append(info)
# print(gastos)
#  print(info['Descricao'])

#Teste 2 - melhor estruturação
lista_gastos = []
def add_gastos(gastos):
    aux = True
    while aux:
        descricao = input('Digite uma descrição: ')
        valor = input('Digite o valor do gasto: ')
        categoria = input('Defina uma categoria : ')
        quest = input('Deseja adicionar mais informação? [S] ou [N]: ')
        info = {
        'Descricao': descricao,
            'Valor': valor,
        'Categoria':categoria
        }
        quest = quest.upper()
        gastos.append(info)
        if quest == 'N':
            aux = False
    
add_gastos(lista_gastos)