from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        conteudo = '--- Iniciando o Preparo ---'
        conteudo += f"\n{self.ferver_agua()}"
        conteudo += f"\n{self.misturar()}"
        conteudo += f"\n{self.servir()}"
        conteudo += '\n--- Bebida Pronta ---'
        print(conteudo)
        
    def ferver_agua(self):
        return '1. Fervendo água a 100 graus Celsius.'
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):        
    def misturar(self):
        return '2. Passando água Pressurizada pelo pó de café moído.'
    
    def servir(self):
        return '3. Servindo em xícara pequena.'

class Cha(BebidaQuente):
    def misturar(self):
        return '2. Mergulhando o sachê de ervas na água.'
    
    def servir(self):
        return '3. Servindo em uma caneca de Porcelana com limão.'

class Leite(BebidaQuente):
    def misturar(self):
        return '2. Passando vapor pressurizado pelo bico de leite.'
    
    def servir(self):
        return '3. Servindo na caneca grande, já com café.'
