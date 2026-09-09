from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self,lados):
        self.qtd_lados = lados
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        self.lado = lados
        
    def perimetro(self):
        perimetro = 4 * self.lado
        return perimetro
    
    def area(self):
        area = self.lado ** 2 
        return area

class Circulo(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        self.raio = lados
        
    def perimetro(self):
        perimetro = (self.raio * 2) * 3.14
        return perimetro
        
    def area(self):
        area = (self.raio ** 2) * 3.14
        return area