from datetime import datetime
from pessoa import Cliente, PessoaFisica
from conta import Conta, ContaCorrente
from historico import Historico
from transacao import Deposito, Saque


#* Menu
menu_acessos = '''
[1] Criar Cliente e Conta
[2] Listar Contas
[3] Acessar Cliente
[4] Sair

==> '''

menu_operações = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==> """

def registrar_endereço():
    logradouro = input("---Informe o Seu logradouro---\n-> ")
    numero = input("---Informe o número do seu endereço---\n-> ")
    bairro = input("---Informe o seu bairro---\n-> ")
    cidade = input("---Informe a sua cidade---\n-> ")
    estado = input("---Informe a sigla do seu estado---\n-> ")
    endereco_completo = (f"Rua: {logradouro},{numero} - Bairro: {bairro} - Cidade: {cidade}/{estado}")
    return endereco_completo

def corrigir_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        print("\n Por favor, insira um valor válido.\n Exemplo: 12312312346\n")

    return cpf

def login_cliente(clientes):
    cpf = corrigir_cpf(input("\nPor favor informe o seu CPF:\n-> "))
    palavra = input("Por favor, informe sua palavra secreta:\n-> ")
    cliente = checar_cpf(cpf, clientes)

    if cliente and cliente.passkey == palavra:
        print(f"\nBem-vindo, {cliente.nome}!\n")
        return cliente

def checar_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return 

def criar_cliente(clientes):
    while True:
        cpf = corrigir_cpf(input("\nPor favor informe o seu CPF:\n-> "))
        if checar_cpf(cpf, clientes = clientes):
            print("\nJá existe um cliente cadastrado com esse CPF!\n")
            continue

        nome = input ("\nPor favor informe o seu nome completo:\n-> ")
        if not nome.strip():
            print("\nO nome não pode ser vazio! \n")

        data_de_nascimento = input ("\nPor favor informe a sua data de nascimento:\n-> ")
        try:
            datetime.strptime(data_de_nascimento, "%d/%m/%Y")
        except ValueError:
            print("\nData de Nascimento inválida, tente novamente\n")
            continue

        endereco = registrar_endereço()

        palavra_secreta = input("Por favor, informe a sua palavra secreta\n-> ")
        if not palavra_secreta.strip():
            print("\n---Palavra secreta não pode ser vazia!---\n")
            continue
        
        teste = PessoaFisica(nome = nome, cpf = cpf, data_de_nascimento = data_de_nascimento, endereco = endereco, passkey= palavra_secreta)

        clientes.append(teste)

        return 


def criar_conta(contas, clientes):
    cpf = corrigir_cpf(input("\nPor favor informe o seu CPF:\n->"))
    cliente = checar_cpf(cpf, clientes= clientes)

    if not cliente:
        print("\n Cliente não encontrado, fluxo de criação incorreto.\n Por favor, tente novamente.")
        return
    
    numero_de_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente = cliente, numero= numero_de_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f"Conta Criada com sucesso!\nnúmero da conta: {conta.numero}\nagência: {conta.agencia}\ncliente: {cliente.nome}\n")


    return clientes,contas

def depositar(cliente):
    conta = cliente.contas[0]
    valor = float(input("\nPor favor informe o valor do depósito:\n->"))    
    transacao = Deposito(valor=valor)
    
    cliente.realizar_transacao(conta = conta, transacao = transacao)
    return cliente

def sacar(cliente):
    conta = cliente.contas[0]
    valor = float(input("\nPor favor informe o valor do saque:\n->"))    
    transacao = Saque(valor=valor)

    cliente.realizar_transacao(conta = conta, transacao = transacao)

    return cliente

def extrato(cliente):
    conta = cliente.contas[0]
    print("=" * 90)
    print(f"Extrato da conta {conta.numero} do cliente {cliente.nome}")
    print("=" * 90)
    if not conta.historico.transacoes:
        print("| Nenhuma transação realizada.")
    else:
        for t in conta.historico.transacoes:
            print(f"| {t['tipo']:<10} | Valor: R$ {t['valor']:<10.2f} | Data: {t['data']}")
    print("=" * 90)
    print(f"| Saldo atual: R$ {conta.saldo():.2f}")
    print("=" * 90)

def main():
    contas = []
    clientes = []
    while True:
        #* Inicialização
        escolher_menu = input(menu_acessos)
        #menu_acessos
        if escolher_menu == "1":
            criar_cliente(clientes)
            criar_conta(contas, clientes)

        #* Listar contas
        elif escolher_menu == "2":
            if not contas:
                print("\nNenhuma conta cadastrada.\n")
            else:
                for conta in contas:
                    print(Conta.__str__(conta))

        #* Acessar cliente
        elif escolher_menu == "3":
            if not clientes:
                print("\nNenhum cliente cadastrado.\n")
            else:
                cliente = login_cliente(clientes)
                if not cliente:
                    print("\nCliente não encontrado ou palavra secreta incorreta.\n")
                    continue
                while True:
                    #* Menu de operações
                    print("\nSelecione uma operação:")
                    escolher_operação = input(menu_operações)

                    #Depositar
                    if escolher_operação == "1":
                        depositar(cliente)

                    #Sacar
                    elif escolher_operação == "2":
                        sacar(cliente)

                    #Extrato
                    elif escolher_operação == "3":
                        extrato(cliente)

                    #Sair
                    elif escolher_operação == "4":
                        break
                    else:
                        print("\nOpção inválida, tente novamente.\n")
        #sair
        elif escolher_menu == "4":
            print("\nObrigado por utilizar nosso sistema bancário!\n")
            break
        else:
            print("\nOpção inválida, tente novamente.\n")


main()