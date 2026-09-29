from rich import print
from rich.panel import Panel
import emoji

class Mensagem:
    def __init__(self,msg:str,tipo = 'AVISO',icone = ':left_speech_bubble:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone
        
    def mostrar(self):
        caixa = Panel(self._mensagem,title=f'{self._icone:<2} {self._tipo:^2} {self._icone:>2}',width=50,style='white on black')
        print(caixa)
    
class Erro(Mensagem):
    def __init__(self, msg,tipo='ERRO' ,icone=":prohibited:"):
        super().__init__(msg,tipo,icone)
        self._tipo = tipo
        self._icone = icone
        
    def mostrar(self):
        caixa = Panel(self._mensagem,title=f'{self._icone:<2} {self._tipo:^2} {self._icone:>2}',width=50,style='yellow on red')
        print(caixa)

class Alerta(Mensagem):
    def __init__(self, msg,tipo= 'ALERTA',icone= ':warning:'):
        super().__init__(msg,tipo,icone)
        self._tipo = tipo
        self._icone = icone
        
    def mostrar(self):
        caixa = Panel(self._mensagem,title=f'{self._icone:<2} {self._tipo:^2} {self._icone:>2}',width=50,style='black on yellow')
        print(caixa)