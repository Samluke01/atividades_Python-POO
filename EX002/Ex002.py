# Declaração de classes
class Gafanhoto:
    """
    Essa Classe cria um cadastro de um Gafanhoto, 
    que é uma pessoa!
    
    para criar um novo Gafanhoto(a) use:
    Variavel = Gafanhoto(nome, idade)
    """
    def __init__(self,nome = 'Fulano',idade = 0): # Metodo Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade
        
    # Metodos de Instancia 
    def aniversrio(self):
        self.idade += 1
    
    def __str__(self):  # Dunder Mithod
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} anos de Idade!"



# Declaração de Objetos
g1=Gafanhoto('Gabriel',27)
g1.aniversrio()
print(g1)
print(g1.__doc__)   # Dunder Attribute


''' Dunder Mithod possui parenteses no fim
__str__()
__gatestate__()
'''

''' Dunder Attribute não possui parenteses no fim
__dict__
__doc__
__class__
'''