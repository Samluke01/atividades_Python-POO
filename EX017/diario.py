from rich import print
class Diario:
    def __init__(self, senha = 'De@thMet@l'):
        self.__segredos = []
        self.__senha = senha.strip()
                
    def escrever(self,msg):
        if type(msg) == str:
            self.__segredos.append(msg.strip())
    
    def ler(self,senha = None):
        if senha == None or senha != self.__senha:
            raise PermissionError('Senha incorreta')
        else:
            print('[green]Diário Liberado')
            for c in self.__segredos:
                print(f'- {c}')
                
    @property
    def senha(self):
        raise PermissionError('Ninguem Tem Permissão de ver a senha')
        
    @senha.setter
    def senha(self,senhaNova):
        self.__senha = senhaNova.strip()
        