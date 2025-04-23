# // Importando bibliotecas para o projeto
from datetime import datetime
import pytz

# ! Menu principal
menu_principal = '''
[1] Criar Usuário
[2] Criar conta corrente
[3] Acessar Usuário
[4] Sair

==> '''

# ! Menu secundário
menu_secundário = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

usuários = []
contas_correntes = []

def criar_conta_corrente(contas):
    conta_corrente = input("Por favor, informe sua conta corrente")

    contas.append({"Conta Corrente": conta_corrente})

    print(contas)

#* Fortamação de endereço
def registrar_endereço():
    logradouro = input("---Informe o Seu logradouro---\n-> ")
    numero = input("---Informe o número do seu endereço---\n-> ")
    bairro = input("---Informe o seu bairro---\n-> ")
    cidade = input("---Informe a sua cidade---\n-> ")
    estado = input("---Informe a sigla do seu estado---\n-> ")
    endereco_completo = (f"Rua: {logradouro},{numero} - Bairro: {bairro} - Cidade: {cidade}/{estado}")
    return endereco_completo

#* Checar CPF repetido
def checar_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            return True  # CPF já cadastrado
    return False  # CPF não encontrado


    
    

#* Precisa de nome, data de nascimento, cpf e endereço
def criar_usuário(clientes, contas):
    cpf = input("Por favor informe CPF\n-> ")

    # Checar se o CPF já existe
    if checar_cpf(cpf, clientes):
        print("\n---CPF já cadastrado! Não é possível criar usuário com este CPF.---\n")
        return  # Interrompe a criação do usuário

    nome = input("Por favor informe Nome\n-> ")
    data_de_nascimento = input("Por favor informe Data de nascimento\n-> ")
    endereço = registrar_endereço()
    
    clientes.append({"Nome": nome, "Data_de_Nascimento": data_de_nascimento, "CPF": cpf, "Endereço": endereço})
    print("\n---Usuário criado com sucesso!---\n")

# Função para obter hora
def obter_data():
    data_fuso_horario = pytz.timezone("America/Sao_Paulo")
    return datetime.now(data_fuso_horario).strftime("%d/%m/%Y %H:%M")

# Função para verificar limite de transações
def verificar_limite_transacoes(total, limite):
    if total >= limite:
        print("\n---Limite atingido!---\n")
        return False  # Limite atingido
    return True  # Ainda permitido

# Função para realizar depósito
def efetuar_deposito(valor, saldo, depositos, total_de_transacoes):
    saldo_atual = saldo
    transacao = total_de_transacoes

    if valor > 0:
        saldo_atual += valor
        depositos.append({"Valor": valor, "Data/Hora": obter_data()})
        transacao += 1
        print("\n---Valor depositado com sucesso!---\n")
    else:
        print("\n---Por favor, insira um valor válido e positivo para efetuar a operação---\n")
    
    return {"saldo": saldo_atual, "transacao": transacao}

# Função para realizar saque
def efetuar_saque(valor, saldo, saques, total_de_saques):
    saldo_atual = saldo
    saques_realizados = total_de_saques

    if valor <= 0:
        print("\n---Por favor, insira um valor válido e positivo para efetuar a operação---\n")
    elif saldo_atual - valor < 0:
        print("\n---Por favor, insira um valor que respeite o seu saldo atual---\n")
    elif valor > 0:
        if valor > 500:
            print("\n---Por favor, respeite o limite de saque de R$ 500,00---\n")
        else:
            saldo_atual -= valor
            saques.append({"Valor": valor, "Data/Hora": obter_data()})
            saques_realizados += 1
            print("\n---Valor sacado com sucesso!---\n")
    return {"saldo": saldo_atual, "saques_realizados": saques_realizados}

# Função para mostrar o extrato
def mostrar_extrato(depositos, saques, saldo):
    saldo_atual = saldo
    lista_de_depositos = depositos
    lista_de_saques = saques

    if saldo_atual == 0: 
        print("Sem saldo disponível para o extrato")
    else:
        print(" Extrato ".center(50, "="))

        for lista_de_deposito in lista_de_depositos:
            print(f"|    Depósito: R${lista_de_deposito['Valor']:.2f} Data/Hora: {lista_de_deposito['Data/Hora']}")
        
        print("|", "-" * 48)
        for lista_de_saque in lista_de_saques:
            print(f"|    Saque:    R${lista_de_saque['Valor']:.2f} Data/Hora: {lista_de_saque['Data/Hora']}")
        print("|", "-" * 48)
        print(f"|    Seu saldo é: R${saldo:.2f}")
        print("=" * 50)

# Função principal
def _main():
    # * Variáveis das operações básicas (Saque, Depósito e Extrato)
    saldo = 0
    total_de_saques = 0  # Contagem de saques no total
    total_de_transacoes = 0  # Contagem de transações no total

    # * Constantes das operações básicas (Saque e Depósito)
    LIMITE_DE_SAQUE = 3  # Limite de saques
    LIMITE_DE_TRANSACOES_POR_DIA = 10  # Limite de transações

    # * Listas de registro (Depósitos, Saques, Clientes e Contas)
    registro_depositos = []  # Armazena Data/Hora + Depósito
    registro_saques = []  # Armazena Data/Hora + Saque

    # * Registro de conta corrente e usuário
    usuários = []
    contas_correntes = []

    while True:
        escolha_menu = input(menu_principal)

        if escolha_menu == "1":
            criar_usuário(usuários, None)

        elif escolha_menu == "2":
            criar_conta_corrente(contas=contas_correntes)

        elif escolha_menu == "3":
            print("Acessar usuário")

            while True:

                escolha = input(menu_secundário)

                if escolha == "d":
                    print("\n---Opção de Depósito selecionada---\n")
                    if not verificar_limite_transacoes(total_de_transacoes, LIMITE_DE_TRANSACOES_POR_DIA):
                        continue  # Volta ao menu principal sem executar a operação
                    try:
                        valor_depósito = int(input("\n---Insira o valor desejável para o depósito---\n-> "))
                        resultado = efetuar_deposito(valor_depósito, saldo, registro_depositos, total_de_transacoes)
                        saldo = resultado['saldo']
                        total_de_transacoes = resultado['transacao']
                        print(f"Total de transações realizadas: {total_de_transacoes}")
                    except ValueError:
                        print("\n---Por favor, insira um valor válido---\n")

                elif escolha == "s":
                    print("\n---Opção de Saque selecionada---\n")
                    if not verificar_limite_transacoes(total_de_saques, LIMITE_DE_SAQUE):
                        print("\n---Você já atingiu o limite de 3 saques diários!---\n")
                        continue  # Volta ao menu principal sem executar a operação
                    try:
                        valor_saque = int(input("\n---Insira o valor desejável para o saque---\n-> "))
                        resultado = efetuar_saque(valor_saque, saldo, registro_saques, total_de_saques)
                        saldo = resultado['saldo']
                        total_de_saques = resultado['saques_realizados']
                        print(f"Total de saques realizados: {total_de_saques}")
                    except ValueError:
                        print("\n---Por favor, insira um valor válido---\n")

                elif escolha == "e":
                    print("\n---Opção de Extrato selecionada---\n")
                    mostrar_extrato(registro_depositos, registro_saques, saldo)

                elif escolha == "q":
                    print("\n---Obrigado por utilizar nosso banco!---\n")
                    break

                else:
                    print("\n---Por favor, insira um valor válido---\n")

        elif escolha_menu == "4":
            break


_main()
