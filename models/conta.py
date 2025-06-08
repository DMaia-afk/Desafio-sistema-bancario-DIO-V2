from historico import Historico

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero): #bool
        return cls(cliente, numero)

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico


    def sacar(self, valor): #bool
        saldo = self._saldo

        if saldo < valor:
            print("Saldo insuficiente")
            return False
        else:
            saldo -= valor
            print(f"Saque de {valor} realizado com sucesso")
            return True

    def depositar(self, valor): #bool
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado com sucesso")
            return True
        else:
            print("Valor inválido")
            return False

    def saldo(self):
        return self._saldo


    def __str__(self):
        return f"""\
            ===============================
            Conta do Cliente:
            ===============================
            Agência: {self._agencia}
            Conta: {self._numero}
            Saldo: {self._saldo}
            ===============================
        """

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        numero_de_saques = len([
                valor for transacao in self.historico.transacoes if transacao['tipo'] == "Saque"
        ])
        valor_excedido = valor > self._limite
        numero_de_saques_excedido = numero_de_saques >= self._limite_saques
        
        if valor_excedido:
            print("Valor maior que o limite permitido")
            return False
        elif numero_de_saques_excedido:
            print("Número de saques excedido")
            return False
        elif self.saldo() < valor:
            print("Saldo insuficiente")
            return False
        
        else:
            self._saldo -= valor
            print(f"Saque de {valor} realizado com sucesso")
            return True
        

    def depositar(self, valor):
        return super().depositar(valor)
