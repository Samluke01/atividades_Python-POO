from abc import ABC,abstractmethod
import re

class Validador(ABC):
    def __init__(self):
        self.str = None
        
    @abstractmethod    
    def validador(self):
        pass
    
class Usuario(Validador):
    def validador(self,msg:str):
        if re.search('[A-Z]',msg) or re.search(r"\s", msg):
            return 'Não'
        if 5<=len(msg)<=20:
            if re.search(f'[0-9]',msg):
                if re.search(f'_',msg):
                    return 'Sim'
                else:
                    return 'Sim'
            else:
                return 'Sim'
        else:
            return 'Não'
        
class Senha(Validador):
    def validador(self,msg:str):
        if re.fullmatch('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%&?*]).{8,}$',msg):
            return 'Sim'
        else:
            return 'Não'
        
class Email(Validador):
    def validador(self,msg:str):
        if re.fullmatch("^[a-z0-9.%+-]+@[a-z0-9.]+\.[a-z0-9]{2,}$",msg):
            return 'Sim'
        else:
            return 'Não'
    
def validador_dado(Validador,msg):
    res = Validador.validador(msg)
    print(f'Valor: {msg} é um valor válido? {res}')