from alocacoes import *

def menu_login():
    print("Bem-vindo ao Menu de Login!")
    print("1 - Login como admin")
    print("2 - Login como funcionário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        login_admin()
    elif opcao == "2":
        menu()
    elif opcao == "3":
        exit()
    else:
        print("Opção inválida.")
        menu_login()

def login_admin():
    print("Login admin (...)")
    senha = input("Insira a senha: ")
    if senha == "admin123":
        menu_admin()
    else: 
        print("Senha inválida!")

def menu_admin():
    while True:
        print("1 - Adicionar funcionário")
        print("2 - Editar funcionário")
        print("3 - Consultar funcionário")
        print("4 - Remover funcionário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            consultar_funcionario()
        elif opcao == "3":
            cpf = input("CPF do funcionario: ")
            editar_funcionario(cpf)
        elif opcao == "4":
            cpf = input("CPF do funcionario: ")
            remover_funcionario(cpf)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu():
    while True:
        print("1 - Adicionar cliente")
        print("2 - Editar cliente")
        print("3 - Consultar clientes")
        print("4 - Remover cliente")
        print("5 - Adicionar veículo")
        print("6 - Editar veículo")
        print("7 - Consultar veículos")
        print("8 - Remover veículo")
        print("9 - Adicionar locação")
        print("10 - Consultar locações")
        print("11 - Remover locação")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            consultar_cliente()
        elif opcao == "3":
            cpf = input("CPF do cliente: ")
            editar_cliente(cpf)
        elif opcao == "4":
            cpf = input("CPF do cliente: ")
            remover_cliente(cpf)
        elif opcao == "5":
            adicionar_veiculo()
        elif opcao == "6":
            consultar_veiculo()
        elif opcao == "7":
            placa = input("Placa do veículo: ")
            editar_veiculo(placa)
        elif opcao == "8":
            placa = input("Placa do veículo: ")
            remover_veiculo(placa)
        elif opcao == "9":
            adicionar_locacao()
        elif opcao == "10":
            consultar_locacoes()
        elif opcao == "11":
            cpf = input("CPF do cliente: ")
            placa = input("Placa do veículo: ")
            remover_locacao(cpf, placa)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

menu_login()

