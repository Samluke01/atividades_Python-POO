from hashlib import sha256
from rich import print

class Credencial():
    def __init__(self):
        self.__hash = None
        
    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self,senhaNova):
        if len(senhaNova) <= 4:
            raise ValueError('Senha Inválida!') 
        else:
            self.__hash = sha256(senhaNova.encode('utf-8')).hexdigest()
    def validar(self,chave):
        if sha256(chave.encode('utf-8')).hexdigest() == self.__hash:
            print('Senha CONFIRMADA!')
            return True
        else:
            print('Senha INCORRETA!')
            return False