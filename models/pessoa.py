from datetime import datetime


class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if transacao.registrar(conta):
            conta.historico.transacoes.append({
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_de_nascimento,endereco, passkey):
        super().__init__(endereco)
        self._passkey = passkey
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento

    @property
    def passkey(self):
        return self._passkey