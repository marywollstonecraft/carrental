from datetime import date, timedelta # importa as classes date e timedelta do módulo datetime

# lista para armazenar os objetos das classes
funcionarios = []
clientes = []
veiculos = []
locacoes = []

class Usuario: # define a superclasse Usuario
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

class Funcionario(Usuario): # define a classe Funcionario que herda de Usuario
    def __init__(self, nome: str, cpf: str, cargo: str):
        super().__init__(nome, cpf)
        self.cargo = cargo
        
def adicionar_funcionario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    funcionario = Funcionario(nome, cpf, cargo)
    funcionarios.append(funcionario) # adiciona objeto na lista de funcionarios 
    print("Funcionário adicionado.")

def editar_funcionario(cpf):
    for funcionario in funcionarios: # acessa o funcionario na lista e edita seus atributos
        if funcionario.cpf == cpf:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cargo = input("Cargo: ")
            funcionario.nome = nome
            funcionario.cpf = cpf
            funcionario.cargo = cargo
            print("Edição concluída.")
            return
    print("Funcionário não encontrado.")

def consultar_funcionarios(): # printa os atributos do funcionário armazenado na lista
    for funcionario in funcionarios:
        print("Nome:", funcionario.nome)
        print("CPF:", funcionario.cpf)
        print("Cargo:", funcionario.cargo)

def remover_funcionario(cpf):
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionarios.remove(funcionario)
            print("Funcionário removido.")
            return
    print("Funcionário não encontrado.")
    



class Cliente(Usuario): # define a classe Cliente que herda de Usuario
    def __init__(self, nome: str, cpf: str, cnh: str):
        super().__init__(nome, cpf)
        self.cnh = cnh
        
def adicionar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cnh = input("CNH: ")
    cliente = Cliente(nome, cpf, cnh)
    clientes.append(cliente)
    print("Cliente adicionado com sucesso.")

def editar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cnh = input("CNH: ")
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.cnh = cnh
            print("Cliente editado.")
            return
    print("Cliente não encontrado.")

def consultar_clientes():
    for cliente in clientes:
        print("Nome:", cliente.nome)
        print("CPF:", cliente.cpf)
        print("CNH:", cliente.cnh)

def remover_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)
            print("Cliente removido.")
            return
    print("Cliente não encontrado.")


class Veiculo: # define a classe Veiculo
    def __init__(self, modelo: str, placa: str, cor: str, diaria: float):
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.diaria = diaria
        self.disponivel = True

def adicionar_veiculo():
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    diaria = float(input("Diária: "))
    veiculo = Veiculo(placa, modelo, cor, diaria)
    veiculos.append(veiculo)
    print("Veículo adicionado com sucesso.")
    
def editar_veiculo(placa):
    for veiculo in veiculos: # acessa o veiculo na lista e edita seus atributos
        if veiculo.placa == placa:
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            diaria = float(input("Diária: "))
            veiculo.placa = placa
            veiculo.modelo = modelo
            veiculo.cor = cor
            veiculo.diaria - diaria
            print("Edição concluída.")
            return
    print("Veículo não encontrado.")

def consultar_veiculos():
    for veiculo in veiculos:
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Cor:", veiculo.cor)
        print("Diária:", veiculo.diaria)
        print("Disponível:", "Sim" if veiculo.disponivel else "Não")

def remover_veiculo(placa):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            if not veiculo.disponivel:
                print("Não é possível remover um veículo que está alocado ou reservado.")
                return
            veiculos.remove(veiculo)
            print("Veículo removido com sucesso.")
            return
    print("Veículo não encontrado.")

class Locacao:
    def __init__(self, cliente, veiculo, data_inicio, data_fim, valor):
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor = valor

def adicionar_locacao():
    cpf = input("CPF do cliente: ")
    cliente = buscar_cliente(cpf)
    if cliente is None:
        print("Cliente não encontrado.")
        return
    placa = input("Placa do veículo: ")
    veiculo = buscar_veiculo(placa)
    if veiculo is None:
        print("Veículo não encontrado.")
        return
    data_inicio = input("Data de início (dd/mm/aaaa): ")
    data_fim = input("Data de fim (dd/mm/aaaa): ")
    valor = calcular_valor(data_inicio, data_fim, veiculo.diaria)
    locacao = Locacao(cliente, veiculo, data_inicio, data_fim, valor)
    veiculo.disponivel = False
    locacoes.append(locacao)
    print("Locação adicionada com sucesso.")

def consultar_locacoes():
    for locacao in locacoes:
        print("Cliente:", locacao.cliente.nome)
        print("CPF:", locacao.cliente.cpf)
        print("Veículo:", locacao.veiculo.modelo)
        print("Placa:", locacao.veiculo.placa)
        print("Data de início:", locacao.data_inicio)
        print("Data de fim:", locacao.data_fim)
        print("Valor:", locacao.valor)

def remover_locacao(cpf, placa):
    for locacao in locacoes:
        if locacao.cliente.cpf == cpf and locacao.veiculo.placa == placa:
            locacoes.remove(locacao)
            locacao.veiculo.disponivel = True
            print("Locação removida com sucesso.")
            return
    print("Locação não encontrada.")

def calcular_valor(data_inicio, data_fim, diaria):
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y") # converte as datas p objeto datetime
    data_fim = datetime.strptime(data_fim, "%d/%m/%Y") # metodo strptime do módulo datetime
    dias = (data_fim - data_inicio).days + 1 # calcula o numero de dias usando a prop days
    valor = dias * diaria
    return valor

