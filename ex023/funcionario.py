from abc import ABC,abstractmethod

class Funciopnario(ABC):
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario
        
    @abstractmethod
    def calcular_bonus(self):
        pass
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        if valor is None:
            raise ValueError('impossivel alterar o salario deste jeito!')
        elif valor < self.__salario:
            raise ValueError('Não é permitido redução salarial')
        else:
            self.__salario = valor
        
    def __str__(self):
        return f'{self.nome} ganha R${self.__salario:,.2f} e por ser {self.__class__.__name__} o bonus será de R${self.calcular_bonus():,.2f}'
    
class Gerente(Funciopnario):
    def calcular_bonus(self):
        return self.salario * 0.15
        
class Designer(Funciopnario):
    def calcular_bonus(self):
            return self.salario * 0.08
        
class Desenvolvedor(Funciopnario):
    def calcular_bonus(self):
            return self.salario * 0.1