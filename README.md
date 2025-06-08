# 💰 Desafio Sistema Bancário DIO V2  

Projeto focado na atualização e aprimoramento do sistema bancário da DIO, agora com funcionalidades de **cadastro de clientes** e **criação de contas correntes**.  

## 🎯 Objetivo  

Desenvolver funções para operações bancárias essenciais, garantindo um sistema mais estruturado e eficiente:  

- **Sacar** (`def_saque`) → Recebe argumentos apenas por nome (**keyword only**).  
- **Depositar** (`def_deposito`) → Recebe argumentos apenas por posição (**positional only**).  
- **Visualizar histórico** (`def_extrato`) → Aceita argumentos por posição e nome (**positional only & keyword only**).  

Além disso, serão adicionadas duas novas funções:  

✅ **Cadastro de usuário (cliente)**  
✅ **Criação de conta corrente**  

## 👤 Cadastro de Usuário  

Os usuários serão armazenados em uma lista, com os seguintes dados:  

- **Nome**  
- **Data de nascimento**  
- **CPF** (apenas números, sem repetições)  
- **Endereço** (formato: `logradouro, número - bairro - cidade / UF`)  

⚠️ **Importante**: O CPF é único e não pode ser cadastrado mais de uma vez.  

## 🏦 Criação de Conta Corrente  

As contas também serão armazenadas em uma lista, sendo compostas por:  

- **Agência** (`0001` - valor fixo)  
- **Número da conta** (sequencial, iniciando em `1`)  
- **Usuário vinculado**  

📌 **Um usuário pode ter várias contas, mas cada conta pertence a apenas um usuário.**  

### 🔎 Dica  

Para vincular um usuário a uma conta, basta **filtrar a lista de usuários** pelo número do CPF informado.  

---

## 🖥️ Implementação em Python  

```python
# 💰 Desafio Sistema Bancário DIO V2  

# 🏦 Sistema Bancário com Cadastro de Usuário e Contas  

# Lista para armazenar usuários
usuarios = []

# Lista para armazenar contas bancárias
contas = []

# Função para cadastrar um usuário
def cadastrar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str):
    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("❌ CPF já cadastrado!")
            return
    # Criar e armazenar o usuário
    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("✅ Usuário cadastrado com sucesso!")

# Função para criar uma conta corrente
def criar_conta_corrente(cpf: str):
    # Filtrar usuário pelo CPF
    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario_existente:
        print("❌ Usuário não encontrado!")
        return
    # Criar e armazenar conta
    numero_conta = len(contas) + 1
    conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario_existente}
    contas.append(conta)
    print(f"✅ Conta criada com sucesso! Número da conta: {numero_conta}")

# Função para sacar dinheiro
def saque(*, saldo: float, valor: float):
    if valor > saldo:
        print("❌ Saldo insuficiente!")
    else:
        saldo -= valor
        print("✅ Saque realizado!")
    return saldo

# Função para depositar dinheiro
def deposito(saldo, valor, /):
    saldo += valor
    print("✅ Depósito realizado!")
    return saldo

# Função para visualizar extrato bancário
def extrato(saldo, /, *, transacoes: list):
    print(f"\n📜 Extrato:\nSaldo atual: R${saldo:.2f}")
    print("Transações:")
    for transacao in transacoes:
        print(f"- {transacao}")

# Exemplo de uso
cadastrar_usuario("João Silva", "01/01/1990", "12345678900", "Rua das Flores, 123 - Centro - São Paulo/SP")
criar_conta_corrente("12345678900")

saldo_atual = 1000
saldo_atual = saque(saldo=saldo_atual, valor=200)
saldo_atual = deposito(saldo_atual, 500)
extrato(saldo_atual, transacoes=["Depósito de R$500", "Saque de R$200"])