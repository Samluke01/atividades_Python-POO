from hashlib import sha256

class ContaBancaria:
    """
    Cria uma Conta bancaria
    permite fazer Saques e Depositos

    """
    def __init__(self, id, nome, saldo = 0, senha = None):
        self._id = id  # Publico (+)
        self._titular = nome # Protegido (#)
        self.__saldo = saldo # Privado (-)
        if senha is None:
            senha = self.pede_senha()
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()
        print(f'Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')    
            
    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self,nome):
        self.validar_senha(self.pede_senha())
        if self.validar_senha:
            self._titular = nome         
            
    def __str__(self):
        #return f"A Conta {self.id} de { self.titular} tem R${self.saldo:,.2f} de saldo."
        return f"Estado atual da conta: {self.__dict__}"
    
    def validar_senha(self,chave):
        if self.__hash == sha256(chave.encode('utf-8')).hexdigest():
            return True
        else:
            return False
    
    def pede_senha(self):
        from pwinput import pwinput
        return pwinput('Senha: ')
    
    def sacar(self,valor,chave = None):
        if chave is None:
            self.validar_senha(self.pede_senha())
            if self.validar_senha:
                valor = abs(valor)
                if valor > self.__saldo:
                    print(f"Saque NEGADO... Saldo INSUFICIENTE")
                else:
                    self.__saldo -= valor
                    print(f"Saque de R${valor:,.2f} Autorizado na conta {self._id}")
                    print(f'Conta: {self._id}\nSaldo: {self.__saldo}')
            else:
                print('Senha Negada, Saque Negado!')
        else:
            self.validar_senha(chave)
            if self.validar_senha:
                valor = abs(valor)
                if valor > self.__saldo:
                    print(f"Saque NEGADO... Saldo INSUFICIENTE")
                else:
                    self.__saldo -= valor
                    print(f"Saque de R${valor:,.2f} Autorizado na conta {self._id}")
                    print(f'Conta: {self._id}\nSaldo: {self.__saldo}')
            else:
                print('Senha Negada, Saque Negado!')
                    
        
    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} Autorizado na conta {self._id}")
        print(f'Conta: {self._id}\nSaldo: {self.__saldo}')