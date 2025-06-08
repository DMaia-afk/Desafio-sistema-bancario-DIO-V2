import datetime
class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._trasacoes.append(
        {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d-%m-%Y'),
        })

## Ver possibilidade de gerar relatório similar ao extrato bancário
