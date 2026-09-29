from abc import ABC,abstractmethod
from rich import print

class Arquivo(ABC):
    def __init__(self, nome: str, tamanho: int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho

        
    @abstractmethod
    def abrir(self):
        pass
        
    @property
    def extensao(self):
        return self._extensao
    
    @extensao.setter
    def extensao(self, ext):
        formato = ['pdf','doc','docx']
        ext = ext.lower().strip()
        if ext in formato:
            self._extensao = ext
        else:
            raise AttributeError('O Arquivo esta  em um formato não suportado!')
        
    @property
    def nome_completo(self):
        return f'{self.nome}.{self._extensao}({self.tamanho/1_000_000}MB)'
        
class DOC(Arquivo):
    def __init__(self, nome, tamanho, ext = 'docx'):
        super().__init__(nome, tamanho)
        self.extensao = ext
        
    def abrir(self):
        print(f'Abrindo O Arquivo [blue]"{self.nome_completo}"[/] no  Microsoft Word!')
        
class PDF(Arquivo):
    def __init__(self, nome, tamanho, ext = 'pdf'):
        super().__init__(nome, tamanho)
        self.extensao = ext
        
    def abrir(self):
        print(f'Abrindo O Arquivo [blue]"{self.nome_completo}"[/] no  Adobe Reader!')
        
def abrir_arquivo(Arquivo):
    Arquivo.abrir