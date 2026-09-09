class ContaBancaria:
    """
    Cria uma Conta bancaria
    permite fazer Saques e Depositos

    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        
    def __str__(self):
        return f"A Conta {self.id} de { self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO... Saldo INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} Autorizado na conta {self.id}")
        
    def depositar(self,valor):
        self.saldo += valor     
        print(f"Deposito de R${valor:,.2f} Autorizado na conta {self.id}")
        
        
c1 = ContaBancaria(112,"Gabriel",3000)
c1.sacar(800)
c1.depositar(6820)
print(c1)
#print(c1.__doc__)