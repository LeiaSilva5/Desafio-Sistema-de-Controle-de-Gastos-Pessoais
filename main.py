


# Mostrar gasto médio
def gasto_medio():
    print("Olá,mundo")
# Mostrar total gasto
def total_gasto():
    print("total gasto")
# Listar gastos
def list_gastos():
    print("lista gastos")
# Adicionar gastos
def add_Gastos():
    print("-- Adicionando Gastos --")

# opções do menu
def op_menu(opcao):
    if int(opcao) == 1:
        print('Adicionar Gastos')
    elif int(opcao) == 2:
        print('Listar gastos')
    elif int(opcao) == 3:
        print('Listar gastos')
    elif int(opcao) == 4:
        print('Listar gastos')
    elif int(opcao) == 5:
        print('Listar gastos')
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
    