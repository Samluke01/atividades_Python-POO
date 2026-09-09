from abc import ABC, abstractmethod
from rich import print
import random as rd

class Personagem(ABC):
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.limiteVida = vida
        self.golpes = []
        self.dado = rd.randint(1,6)
        self.ataque = rd.randint(0,2)
        
    def atacar(self,alvo,força):
        if self.vida <= 0 or alvo.vida <= 0:
            print('Comando Inválido!')
        else:
            Dano = rd.randrange(0,força)
            print(f'[green]{self.nome}[/] Ataca [red]{alvo.nome}[/] com [blue]{self.golpes[self.ataque]}[/] de força {Dano}')
            
            self.receber_dano(alvo,Dano)
            
    def receber_dano(self,alvo,dano):
        if alvo.vida <= 0:
            print('Comando Inválido!')
        else:
            alvo.vida -= dano
            print(f'[red]{alvo.nome}[/] tem [orange]{alvo.vida}[/] pontos de vida!')
            
    @abstractmethod
    def curar(self):
        pass
    
class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco','Chute Giratório','Cabeçada']
        
    def curar(self):
        if self.dado <= 2:
            vida = 0.2 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida 
            print(f'[green]{self.nome}[/] enrolou um atadura em seu ferimento e recuperou [yellow]{vida:.0f}[/] de pontos de vida!')
        elif self.dado > 2 and self.dado <= 4 :
            vida = 0.4 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida
            print(f'[green]{self.nome}[/] enrolou um atadura em seu ferimento e recuperou [yellow]{vida:.0f}[/] de pontos de vida!')
        else:
            vida = 0.6 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida
            print(f'[green]{self.nome}[/] enrolou um atadura em seu ferimento e recuperou [yellow]{vida:.0f}[/] de pontos de vida!')
            
            
        if self.vida > self.limiteVida:
            self.vida = self.limiteVida
        
        print(f'[green]{self.nome}[/] tem [orange]{self.vida}[/]')
        
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo','Raio Arcano','Onda de Choque']
        
    def curar(self):
        if self.dado <= 2:
            vida = 0.2 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida 
            print(f'[green]{self.nome}[/] tomou sua poção e recuperou [yellow]{vida}[/] de pontos de vida!')
        elif self.dado > 2 and self.dado <= 4 :
            vida = 0.4 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida
            print(f'[green]{self.nome}[/] tomou sua poção e recuperou [yellow]{vida}[/] de pontos de vida!')
        else:
            vida = 0.6 * self.limiteVida
            vida = rd.randrange(0,vida)
            self.vida += vida
            print(f'[green]{self.nome}[/] tomou sua poção e recuperou [yellow]{vida}[/] de pontos de vida!')
            
            
        if self.vida > self.limiteVida:
            self.vida = self.limiteVida
        
        print(f'[green]{self.nome}[/] tem [orange]{self.vida}[/]')