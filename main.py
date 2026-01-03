# Globais
lista_gastos = []
# Função que adiciona gastos
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


# opções do menu
def op_menu(opcao):
    if int(opcao) == 1:
        add_gastos(lista_gastos)
    elif int(opcao) == 2:
        print('Listar gastos')
    elif int(opcao) == 3:
        print('Mostrar gastos  total')
    elif int(opcao) == 4:
        print('Mostrar gasto médio')
    else:
        print('Opção invalida, deseja retornar par o menu inicial ? [S] [N]')
        item = input(": ")
        if item.upper() == 'S':
            menu()
        elif item.upper() == 'N':
            print("Até mais!")    

# Menu principal
def menu():
    validador = True
    while validador:
        print("----- Sistema de Controle de Gastos Pessoais -----")
        print("Digite uma opção abaixo: ")
        print("1 - Adicionar gasto \n2 - Listar gastos \n3 - Mostrar total gasto \n4 - Mostrar gasto médio \n5 - Sair")
        op = input("Digite aqui: ") 
        if int(op) == 5:
            print("Até mais !")
            validador = False   
        else:
            op_menu(op)
        
            
menu()
    