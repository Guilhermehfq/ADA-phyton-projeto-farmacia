# Bibliotecas importadas
from datetime import datetime

# Classes
# Classe / Gerenciador de clientes ----------------------------------------------------------------------------------------------


class Cliente:
    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idoso = self.calcular_idoso()

    def calcular_idoso(self) -> bool:
        data_atual = datetime.now()
        ano_nascimento = int(self.data_nascimento.split("/")[-1])
        ano_atual = data_atual.year

        idade = ano_atual - ano_nascimento
        return idade > 65


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

# Classe / Gerenciador de medicamentos ----------------------------------------------------------------------------------------------


class Medicamento:
    def __init__(self, nome: str, composto_principal: str, descricao: str, valor_unitario: float):
        self.nome = nome
        self.composto_principal = composto_principal
        self.descricao = descricao
        self.valor_unitario = valor_unitario


class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, composto_principal, descricao, valor_unitario, necessita_receita: bool):
        super().__init__(nome, composto_principal, descricao, valor_unitario)
        self.necessita_receita = necessita_receita


class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome: str, composto_principal: str, descricao: str, valor_unitario: float):
        super().__init__(nome, composto_principal, descricao, valor_unitario)


class GerenciadorMedicamentos:
    def __init__(self):
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

# Classe / Gerenciador de lavoratorios ----------------------------------------------------------------------------------------------


class Laboratorio:
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
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

# Classe / Gerenciador de vendas ----------------------------------------------------------------------------------------------


class Venda:
    def __init__(self, cliente):
        self.data_hora = datetime.now()
        self.cliente = cliente
        self.produtos = []
        self.valor_total = 0

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append({"produto": produto, "quantidade": quantidade})

    def calcular_valor_total(self):
        valor_total = sum(item["produto"].valor_unitario *
                          item["quantidade"] for item in self.produtos)

        if self.cliente.idoso:
            valor_total *= 0.8

        if valor_total > 150 and not self.cliente.idoso:
            valor_total *= 0.9

        self.valor_total = valor_total
        return valor_total


class GerenciadorVendas:
    def __init__(self, gerenciador_clientes, gerenciador_medicamentos):
        self.gerenciador_clientes = gerenciador_clientes
        self.gerenciador_medicamentos = gerenciador_medicamentos
        self.vendas_realizadas = []

    def buscar_medicamento_pelo_nome(self, nome_medicamento):
        todos_medicamentos = list(self.gerenciador_medicamentos.medicamentos_quimioterapicos.values(
        )) + list(self.gerenciador_medicamentos.medicamentos_fitoterapicos.values())
        for medicamento in todos_medicamentos:
            if nome_medicamento.lower() in medicamento.nome.lower():
                return medicamento
        return None

    def realizar_venda(self):
        cpf_cliente = input("Digite o CPF do cliente: ")
        cliente = self.gerenciador_clientes.clientes.get(cpf_cliente)
        if not cliente:
            print("Cliente não encontrado.")
            return

        venda = Venda(cliente)
        medicamentos_controlados = []

        while True:
            nome_medicamento = input(
                "Digite o nome do medicamento ou 'fim' para finalizar: ").lower()
            if nome_medicamento == 'fim':
                break

            medicamento = self.buscar_medicamento_pelo_nome(nome_medicamento)
            if not medicamento:
                print("Medicamento não encontrado.")
                continue

            quantidade = int(
                input(f"Digite a quantidade de '{medicamento.nome}' a ser vendida: "))
            venda.adicionar_produto(medicamento, quantidade)
            print(f"'{medicamento.nome}' adicionado à venda.")

            if isinstance(medicamento, MedicamentoQuimioterapico) and medicamento.necessita_receita:
                medicamentos_controlados.append(medicamento.nome)

        valor_total = venda.calcular_valor_total()
        print(f"Valor total da venda: R${valor_total:.2f}")

        if medicamentos_controlados:
            print(
                "Atenção: Verifique a receita para os seguintes medicamentos controlados:")
            for nome_controlado in medicamentos_controlados:
                print(f"- {nome_controlado}")

        self.vendas_realizadas.append({"cliente": cliente, "venda": venda})
        print("Venda realizada com sucesso!")

    def listar_vendas(self):
        vendas_por_cliente = {}

        for venda_info in self.vendas_realizadas:
            cliente = venda_info["cliente"]
            venda = venda_info["venda"]

            if cliente not in vendas_por_cliente:
                vendas_por_cliente[cliente] = []
            vendas_por_cliente[cliente].append(venda)

        print("\n===== LISTA DE VENDAS REALIZADAS =====")
        for cliente, vendas in vendas_por_cliente.items():
            print(f"Cliente: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            for venda in vendas:
                print(f"Data e Hora da Venda: {venda.data_hora}")
                print("Produtos:")
                for item in venda.produtos:
                    print(
                        f"  - {item['produto'].nome}: {item['quantidade']} unidades")
                print(f"Valor Total: R${venda.valor_total:.2f}")
                print("-" * 40)
            print("=" * 40)
        print("=" * 40)

# Gerenciador de relatorios ----------------------------------------------------------------------------------------------


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
        todos_medicamentos_quimioterapicos = list(
            gerenciador_medicamentos.medicamentos_quimioterapicos.values())
        todos_medicamentos_fitoterapicos = list(
            gerenciador_medicamentos.medicamentos_fitoterapicos.values())
        todos_medicamentos = todos_medicamentos_quimioterapicos + \
            todos_medicamentos_fitoterapicos

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
        if quimioterapicos_alfabetica:
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
        if fitoterapicos_alfabetica:
            for remedio in fitoterapicos_alfabetica:
                print(f"Remédio: {remedio.nome}")
                print("-" * 30)
        else:
            print("Nenhum medicamento encontrado.")

    def imprimir_relatorio_diario(self, gerenciador_vendas, gerenciador_medicamentos):
        total_quimioterapico = 0
        total_fitoterapico = 0

        for venda_info in gerenciador_vendas.vendas_realizadas:
            venda = venda_info["venda"]
            for item in venda.produtos:
                medicamento = item["produto"]
                quantidade = item["quantidade"]
                valor_total_item = medicamento.valor_unitario * quantidade

                if isinstance(medicamento, MedicamentoQuimioterapico):
                    total_quimioterapico += valor_total_item
                elif isinstance(medicamento, MedicamentoFitoterapico):
                    total_fitoterapico += valor_total_item
# Verificar qual foi o medicamento mais vendido e em qual quantidade
        medicamento_mais_vendido = None
        quantidade_do_mais_vendido = 0
        valor_total_do_mais_vendido = 0

        for medicamento in gerenciador_medicamentos.medicamentos_quimioterapicos.values():
            medicamento_quantidade_vendida = sum(
                item["quantidade"] for venda_info in gerenciador_vendas.vendas_realizadas
                for item in venda_info["venda"].produtos if item["produto"] == medicamento
            )
            if medicamento_quantidade_vendida > quantidade_do_mais_vendido:
                medicamento_mais_vendido = medicamento
                quantidade_do_mais_vendido = medicamento_quantidade_vendida
                valor_total_do_mais_vendido = medicamento_mais_vendido.valor_unitario * \
                    quantidade_do_mais_vendido

        for medicamento in gerenciador_medicamentos.medicamentos_fitoterapicos.values():
            medicamento_quantidade_vendida = sum(
                item["quantidade"] for venda_info in gerenciador_vendas.vendas_realizadas
                for item in venda_info["venda"].produtos if item["produto"] == medicamento
            )
            if medicamento_quantidade_vendida > quantidade_do_mais_vendido:
                medicamento_mais_vendido = medicamento
                quantidade_do_mais_vendido = medicamento_quantidade_vendida
                valor_total_do_mais_vendido = medicamento_mais_vendido.valor_unitario * \
                    quantidade_do_mais_vendido

# Impressão do relatorio diário

        print("\n===== RELATÓRIO DIÁRIO =====")
        print("Remédio mais vendido:")
        if medicamento_mais_vendido:
            print(f"Nome: {medicamento_mais_vendido.nome}")
            print(f"Quantidade vendida: {quantidade_do_mais_vendido} unidades")
            print(f"Valor total: R${valor_total_do_mais_vendido:.2f}")
        else:
            print("Nenhum medicamento vendido no dia.")

        total_pessoas_atendidas = len(gerenciador_vendas.vendas_realizadas)
        print(f"Quantidade de pessoas atendidas: {total_pessoas_atendidas}")

        print("Número de remédios Quimioterápicos vendidos no dia:")
        print(f"Quantidade vendida: {total_quimioterapico} unidades")
        print(f"Valor total: R${total_quimioterapico:.2f}")

        print("Número de remédios Fitoterápicos vendidos no dia:")
        print(f"Quantidade vendida: {total_fitoterapico} unidades")
        print(f"Valor total: R${total_fitoterapico:.2f}")

        print("=" * 30)

# Menu principal -------------------------------------------------------------------------------------------------------------------------------


def main():
    gerenciador_clientes = GerenciadorClientes()
    gerenciador_medicamentos = GerenciadorMedicamentos()
    gerenciador_laboratorios = GerenciadorLaboratorios()
    gerenciador_relatorios = GerenciadorRelatorios(
        gerenciador_vendas, gerenciador_medicamentos)
    gerenciador_vendas = GerenciadorVendas(
        gerenciador_clientes, gerenciador_medicamentos)

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Medicamento Quimioterápico")
        print("3 - Cadastrar Medicamento Fitoterápico")
        print("4 - Cadastrar Laboratório")
        print("5 - Buscar Cliente por CPF")
        print("6 - Buscar Medicamento por Nome/Laboratório/Descrição")
        print("7 - Realizar Venda")
        print("8 - Exibir Relatório de Vendas")
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
        elif opcao == '7':
            gerenciador_vendas.realizar_venda()
        elif opcao == '8':
            gerenciador_vendas.listar_vendas()
        elif opcao == '9':
            gerenciador_relatorios.imprimir_lista_clientes(
                gerenciador_clientes)
        elif opcao == '10':
            gerenciador_relatorios.imprimir_lista_medicamentos(
                gerenciador_medicamentos)
        elif opcao == '11':
            gerenciador_relatorios.imprimir_lista_medicamentos_quimioterapicos(
                gerenciador_medicamentos)
        elif opcao == '12':
            gerenciador_relatorios.imprimir_lista_medicamentos_fitoterapicos(
                gerenciador_medicamentos)
        elif opcao == '0':
            gerenciador_relatorios.imprimir_relatorio_diario(
                gerenciador_vendas, gerenciador_medicamentos)
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")


# Chamada da função principal
if __name__ == "__main__":
    main()
