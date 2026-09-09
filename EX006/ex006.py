from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Churrasco:
    def __init__(self,titulo,pessoa):
        self.titulo = titulo
        self.pessoas = pessoa
        self.preço = 82.40
        self.consu = 400  / 1000
        
    def analisar(self):
        aComp = self.consu * self.pessoas
        total = self.preço * aComp
        divi = total / self.pessoas
        frase = ""
        frase = f"Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n"
        frase += f"Cada PArticipante comerá {self.consu} e cada Kg custa RS{self.preço:.2f}\n" 
        frase += f"Recomendo [blue]comprar {aComp:.3f}Kg[/] de carne\n"
        frase += f"O custo total será de [green]R${total:,.2f}[/]\n"
        frase += f"Cada Pessoa pagará [yellow]R${divi:.2f}[/] para participar."
        completo = Panel(frase,title=self.titulo,width=60)
        
        print(completo)
        
c1 = Churrasco("Churras dos Parças", 108)
c1.analisar()