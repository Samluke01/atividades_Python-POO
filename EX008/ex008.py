from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,name,nick):
        self.nome = name
        self.nick = nick
        self.games = []
        
    def add_favoritos(self,nome):
        self.games.append(nome)
        self.games.sort()
    
    
    def ficha(self):
        ficha_gamer = f"Nome Real: [black on white] {self.nome} [/]\n"
        ficha_gamer += f"Jogos Favoritos:"
        for c in self.games:
            ficha_gamer += f"\n:video_game: [green]{c}[/]"
        ficha = Panel(ficha_gamer, title=f"jogador <{self.nick}>", width=40)
        print(ficha)
        
        
        
        
c1 = Gamer("Gabriel Barbosa", "Death Metal")
c1.add_favoritos("Star Trek")
c1.add_favoritos("Guitar Hero")
c1.add_favoritos("Star Wars")
c1.add_favoritos("Harry Potter")
c1.ficha()