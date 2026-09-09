from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,distancia,frete):
        self.distancia = distancia
        self.frete = frete
        
    @abstractmethod
    def calcular_frete(self):
        pass
    
class Moto(Transporte):
    def __init__(self, distancia, frete = 0):
        super().__init__(distancia, frete)
        self.fator = 0.50
        
    def calcular_frete(self):
        resposta = self.fator * self.distancia
        return f'R${resposta:.2f}'
    
class Caminhão(Transporte):
    def __init__(self, distancia, frete = 50):
        super().__init__(distancia, frete)
        self.fator = 1.20
        self.fretemin = 50 # minimo de 50km
    
    def calcular_frete(self):
        if self.distancia < self.fretemin:
            return f'Viagem minima de {self.fretemin}Km'
        else:
            resposta = self.fator * self.distancia
            return f'R${resposta:.2f}'
    
class Drone(Transporte):
    def __init__(self, distancia, frete = 10):
        super().__init__(distancia, frete)
        self.fator = 9.50
        self.fretemax = 10 # maximo de 10km
        
    def calcular_frete(self):
        if self.distancia > 10:
            return f'Raio maximo de {self.fretemax}Km'
        else:
            resposta = self.fator * self.distancia
            return f'R${resposta:.2f}'