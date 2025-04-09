# Desafio-sistema-bancario-DIO-V2

Projeto voltado para a atualização e conclusão do projeto bancário da DIO - Agora com cadastro de cliente e criação de conta corrente

## Objetivo Geral

Criar funções para as operações existentes: Sacar, Depositar e visualizar histórico.

* def_saque -> deve receber os argumentos apenas por nome (keyword only).

* def_depósito -> deve receber os argumentos apenas por posição (positional only).

* def_extrato -> deve receber os argumentos por posição e nome (positional only e keyword only).

Criar duas novas funções: Cadastrar usuário (Cliente) e cadastrar conta bancária

* Criar usuário: O programa deve armazenar os usuários em uma lista [] composta por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro,numero - bairro - cidade + sigla do estado. Deve ser armazenado somente os números do CPF. O mesmo CPF não pode ser cadastrado.

* Criar conta corrente -> O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

* Dica -> Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
