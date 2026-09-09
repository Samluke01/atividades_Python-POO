from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.produto = nome
        self.preco = preco
        
    def etiqueta(self):
        etiqueta = Panel(f"[black on white]{self.produto.center(30, "-")}[/]\n{"-"*30}\n[red]{self.preco:,.2f}[/]", title="Produto",style="green",width=34)
        
        print(etiqueta)
    
p1=Produto("Lapis",1980)
p1.etiqueta()