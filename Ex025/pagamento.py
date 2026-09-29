from abc import ABC,abstractmethod
from rich import print
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None
        
    @abstractmethod
    def pagar(self):
        pass
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self,valor):
        if valor >= 0:
            self._valor = valor 
        else:
            raise ValueError('Erro: valores negativos não são permitidos')
   
    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self.valor, grouping=True, symbol=True)

class Boleto(Pagamento):

    def pagar(self,valor):
        self.valor = valor
        
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Boleto Bancario')

class Crédito(Pagamento):

    def pagar(self,valor):
        self.valor = valor
        
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito')

class Pix(Pagamento):

    def pagar(self,valor):
        self.valor = valor
        
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Pix')
        
def finalizar_compra(Pagamento, valor):
    Pagamento.pagar(valor)