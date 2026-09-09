# Declaração de classes
class Gafanhoto:
    def __init__(self): # Metodo Construtor
        # Atributos de Instância
        self.nome = 'Fulano'
        self.idade = 0
        
    # Metodos de Instancia 
    def aniversrio(self):
        self.idade += 1
        
    def mensagem(self):
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} anos de Idade!"



# Declaração de Objetos
g1=Gafanhoto()
g1.nome = 'Gabriel'
g1.idade = 27
g1.aniversrio()
print(g1.mensagem())

g2=Gafanhoto()
g2.nome = 'Maria'
g2.idade = 57
print(g2.mensagem())

g3=Gafanhoto()
g3.nome = 'André'
g3.idade = 80
print(g3.mensagem())