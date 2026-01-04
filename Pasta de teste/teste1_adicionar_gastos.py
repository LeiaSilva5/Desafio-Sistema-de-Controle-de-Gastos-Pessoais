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
# lista_gastos = []
# def add_gastos(gastos):
#     aux = True
#     while aux:
#         descricao = input('Digite uma descrição: ')
#         valor = input('Digite o valor do gasto: ')
#         categoria = input('Defina uma categoria : ')
#         quest = input('Deseja adicionar mais informação? [S] ou [N]: ')
#         info = {
#         'Descricao': descricao,
#             'Valor': valor,
#         'Categoria':categoria
#         }
#         quest = quest.upper()
#         gastos.append(info)
#         if quest == 'N':
#             aux = False
    
# add_gastos(lista_gastos)


# mostrar os gastos armazenados na lista : teste

# my_liat = [
#     {
#         'Descricao': 'Teste 1',
#         'Valor': 21.1,
#         'Categoria':'Valor teste'
#     },
#     {
#         'Descricao': 'Teste 2',
#         'Valor': 22.2,
#         'Categoria':'Valor teste'
#     },
#     {
#         'Descricao': 'Teste 3',
#         'Valor': 23.3,
#         'Categoria':'Valor teste'
#     }

# ]

# contador = len(my_liat)
# print('-------- Lista de gastos --------')
# for i in my_liat:
#     for chave,valor in i.items():
#         print(f'{chave}:{valor}')
#     print('-----------------------------')
# print(my_liat[0]) possível resolver esse problema de outra forma
# print(my_liat[1])
# print(my_liat[2])

# print(len(my_liat))