from abc import ABC

class Funciopnario(ABC):
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario
        
    def calcular_bonus(self):
        self.bonus = self.__salario * self.bonusPC
        return self.bonus
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        if valor < self.__salario:
            raise ValueError('Não é permitido redução salarial')
        else:
            self.__salario = valor
        
    def __str__(self):
        return f'{self.nome} ganha R${self.__salario:,.2f} e por ser {self.__class__.__name__} o bonus será de R${self.calcular_bonus():,.2f}'
    
class Gerente(Funciopnario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonusPc = 0.15
        
class Designer(Funciopnario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonusPc = 0.08
        
class Desenvolvedor(Funciopnario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonusPC = 0.1