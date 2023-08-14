# Bibliotecas importadas
from datetime import datetime

# Classes


class Cliente:
    def __init__(self, cpf: str, nome: str, data_nascimento: str) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idoso = self.calcular_idoso()

    def calcular_idoso(self) -> bool:
        data_atual = datetime.now()
        ano_nascimento = int(self.data_nascimento.split("/")[-1])
        ano_atual = data_atual.year

        idade = ano_atual - ano_nascimento
        return idade >= 60


class GerenciadorClientes:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self):
        cpf = input("Digite o CPF do cliente (somente números): ")
        if cpf in self.clientes:
            print("Cliente já cadastrado com este CPF.")
            return
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input(
            "Digite a data de nascimento do cliente (formato DD/MM/AAAA): ")
        cliente = Cliente(cpf, nome, data_nascimento)
        self.clientes[cpf] = cliente
        print("Cliente cadastrado com sucesso!")

    def buscar_cliente_por_cpf(self):
        cpf_busca = input(
            "Digite o CPF do cliente que deseja buscar (somente números): ")
        cliente = self.clientes.get(cpf_busca)
        if cliente:
            print("\n===== DADOS DO CLIENTE =====")
            print(f"CPF: {cliente.cpf}")
            print(f"Nome: {cliente.nome}")
            print(f"Data de Nascimento: {cliente.data_nascimento}")
            print(f"Idoso: {'Sim' if cliente.idoso else 'Não'}")
            print("=" * 30)
        else:
            print("Cliente não encontrado.")


class Medicamento:
    def __init__(self, nome: str, composto_principal: str, descricao: str, valor_unitario: float) -> None:
        self.nome = nome
        self.composto_principal = composto_principal
        self.descricao = descricao
        self.valor_unitario = valor_unitario


class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, composto_principal, descricao, valor_unitario, necessita_receita: bool) -> None:
        super().__init__(nome, composto_principal, descricao, valor_unitario)
        self.necessita_receita = necessita_receita


class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome: str, composto_principal: str, descricao: str, valor_unitario: float) -> None:
        super().__init__(nome, composto_principal, descricao, valor_unitario)


class GerenciadorMedicamentos:
    def __init__(self) -> None:
        self.medicamentos_quimioterapicos = {}
        self.medicamentos_fitoterapicos = {}

    def cadastrar_medicamento_quimioterapico(self):
        nome = input("Digite o nome do medicamento: ")
        if nome in self.medicamentos_quimioterapicos:
            print("Medicamento já cadastrado com este nome.")
            return
        composto_principal = input(
            "Digite o principal composto do medicamento: ")
        descricao = input("Digite a descrição do medicamento: ")
        valor_unitario = float(
            input("Digite o valor unitário do medicamento em reais: "))
        necessita_receita = input(
            "O medicamento necessita de receita? (S/N): ").upper() == 'S'
        medicamento = MedicamentoQuimioterapico(
            nome, composto_principal, descricao, valor_unitario, necessita_receita)
        self.medicamentos_quimioterapicos[nome] = medicamento
        print("Medicamento quimioterápico cadastrado com sucesso!")

    def cadastrar_medicamento_fitoterapico(self):
        nome = input("Digite o nome do medicamento: ")
        if nome in self.medicamentos_fitoterapicos:
            print("Medicamento já cadastrado com este nome.")
            return
        composto_principal = input(
            "Digite o principal composto do medicamento: ")
        descricao = input("Digite a descrição do medicamento: ")
        valor_unitario = float(
            input("Digite o valor unitário do medicamento em reais: "))
        medicamento = MedicamentoFitoterapico(
            nome, composto_principal, descricao, valor_unitario)
        self.medicamentos_fitoterapicos[nome] = medicamento
        print("Medicamento fitoterápico cadastrado com sucesso!")

    def buscar_medicamento(self):
        termo_busca = input(
            "Digite o termo de busca (nome, composto ou descrição parcial): ").lower()

        medicamentos_encontrados = []

        for medicamento in self.medicamentos_quimioterapicos.values():
            if termo_busca in medicamento.nome.lower() or termo_busca in medicamento.composto_principal.lower() or termo_busca in medicamento.descricao.lower():
                medicamentos_encontrados.append(medicamento)

        for medicamento in self.medicamentos_fitoterapicos.values():
            if termo_busca in medicamento.nome.lower() or termo_busca in medicamento.composto_principal.lower() or termo_busca in medicamento.descricao.lower():
                medicamentos_encontrados.append(medicamento)

        if medicamentos_encontrados:
            print("\n===== MEDICAMENTOS ENCONTRADOS =====")
            for medicamento in medicamentos_encontrados:
                if isinstance(medicamento, MedicamentoQuimioterapico):
                    receita_necessaria = "Sim" if medicamento.necessita_receita else "Não"
                else:
                    receita_necessaria = "Não"
                print(f"Nome: {medicamento.nome}")
                print(f"Composto principal: {medicamento.composto_principal}")
                print(f"Descrição: {medicamento.descricao}")
                print(f"Necessita Receita: {receita_necessaria}")
                print("=" * 30)
        else:
            print("Nenhum medicamento encontrado com o termo de busca.")


class Laboratorio:
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado


class GerenciadorLaboratorios:
    def __init__(self):
        self.laboratorios = {}

    def cadastrar_laboratorio(self):
        nome = input("Digite o nome do laboratório: ")
        if nome in self.laboratorios:
            print("Laboratório já cadastrado com este nome.")
            return
        endereco = input("Digite o endereço do laboratório: ")
        telefone = input("Digite o telefone do laboratório: ")
        cidade = input("Digite a cidade do laboratório: ")
        estado = input("Digite o estado do laboratório: ")
        laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
        self.laboratorios[nome] = laboratorio
        print("Laboratório cadastrado com sucesso!")


class GerenciadorRelatorios:
    def __init__(self) -> None:
        self.lista_alfabetica = []

    def imprimir_lista_clientes(self, gerenciador_clientes):
        lista_alfabetica = sorted(
            gerenciador_clientes.clientes.items(), key=lambda x: x[1].nome)
        for cpf, cliente in lista_alfabetica:
            print(f"Nome: {cliente.nome}")
            print(f"CPF: {cpf}")
            print(f"Data de Nascimento: {cliente.data_nascimento}")
            print(f"Idoso: {'Sim' if cliente.idoso else 'Não'}")
            print("-" * 30)

    def imprimir_lista_medicamentos(self, gerenciador_medicamentos):
        todos_medicamentos_quimioterapicos = list(gerenciador_medicamentos.medicamentos_quimioterapicos.values())
        todos_medicamentos_fitoterapicos = list(gerenciador_medicamentos.medicamentos_fitoterapicos.values())
        todos_medicamentos = todos_medicamentos_quimioterapicos + todos_medicamentos_fitoterapicos

        todos_medicamentos_alfabetica = sorted(
            todos_medicamentos, key=lambda x: x.nome.lower()
        )

        print('Lista de medicamentos\n')
        for medicamento in todos_medicamentos_alfabetica:
            if isinstance(medicamento, MedicamentoQuimioterapico):
                receita_necessaria = "Sim" if medicamento.necessita_receita else "Não"
            else:
                receita_necessaria = "Não"
            print(f"Nome: {medicamento.nome}")
            print(f"Composto principal: {medicamento.composto_principal}")
            print(f"Descrição: {medicamento.descricao}")
            print(f"Necessita Receita: {receita_necessaria}")
            print("=" * 30)
        else:
            print("Nenhum medicamento encontrado.")

    def imprimir_lista_medicamentos_quimioterapicos(self, gerenciador_medicamentos):
        quimioterapicos_alfabetica = sorted(
            gerenciador_medicamentos.medicamentos_quimioterapicos.values(),
            key=lambda x: x.nome.lower()
        )
        print('Lista de medicamentos quimioterapicos\n')
        for remedio in quimioterapicos_alfabetica:
            print(f"Remédio: {remedio.nome}")
            print("-" * 30)
        else:
            print("Nenhum medicamento encontrado.")

    def imprimir_lista_medicamentos_fitoterapicos(self, gerenciador_medicamentos):
        fitoterapicos_alfabetica = sorted(
            gerenciador_medicamentos.medicamentos_fitoterapicos.values(),
            key=lambda x: x.nome.lower()
        )
        print('Lista de medicamentos fitoterápicos\n')
        for remedio in fitoterapicos_alfabetica:
            print(f"Remédio: {remedio.nome}")
            print("-" * 30)
        else:
            print("Nenhum medicamento encontrado.")

# Menu principal


def main():
    gerenciador_clientes = GerenciadorClientes()
    gerenciador_medicamentos = GerenciadorMedicamentos()
    gerenciador_laboratorios = GerenciadorLaboratorios()
    gerenciador_relatorios = GerenciadorRelatorios()

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Medicamento Quimioterápico")
        print("3 - Cadastrar Medicamento Fitoterápico")
        print("4 - Cadastrar Laboratório")
        print("5 - Buscar Cliente por CPF")
        print("6 - Buscar Medicamento por Nome/Laboratório/Descrição")
        # print("7 - Realizar Venda")
        # print("8 - Exibir Relatório de Vendas")
        print("9 - Exibir Relatório de Listagem de Clientes")
        print("10 - Exibir Relatório de Listagem de Medicamentos")
        print("11 - Exibir Relatório de Listagem de Medicamentos Quimioterápicos")
        print("12 - Exibir Relatório de Listagem de Medicamentos Fitoterápicos")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            gerenciador_clientes.cadastrar_cliente()
        elif opcao == '2':
            gerenciador_medicamentos.cadastrar_medicamento_quimioterapico()
        elif opcao == '3':
            gerenciador_medicamentos.cadastrar_medicamento_fitoterapico()
        elif opcao == '4':
            gerenciador_laboratorios.cadastrar_laboratorio()
        elif opcao == '5':
            gerenciador_clientes.buscar_cliente_por_cpf()
        elif opcao == '6':
            gerenciador_medicamentos.buscar_medicamento()
        elif opcao == '9':
            gerenciador_relatorios.imprimir_lista_clientes(
                gerenciador_clientes)
        elif opcao == '10':    
            gerenciador_relatorios.imprimir_lista_medicamentos(gerenciador_medicamentos)
        elif opcao == '11':    
            gerenciador_relatorios.imprimir_lista_medicamentos_quimioterapicos(gerenciador_medicamentos)
        elif opcao == '12':    
            gerenciador_relatorios.imprimir_lista_medicamentos_fitoterapicos(gerenciador_medicamentos)
        # elif para outras opções...
        elif opcao == '0':
            # realizar função para exibir relatório de estatísticas diárias antes de sair
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")


# Chamada da função principal
if __name__ == "__main__":
    main()


# class Vendas:
#  def __init__(self, cliente, produtos) -> None:
#    self.data_hora = datetime.now()
#    self.cliente = cliente
#    self.produtos = produtos
