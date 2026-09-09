from rich import print
from rich.panel import Panel 
from rich.traceback import install

class Controle:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 10
    
    def __init__(self, canal = 1, volume = 2):
        self.canalAtual:int = canal
        self.volumeAtual:int = volume
        self.ligado:bool = False
         
    def liga_desliga(self):
        self.ligado = not self.ligado
        
    def canal_mais(self):
        if self.ligado:
            if self.canalAtual == Controle.canal_max:
                self.canalAtual = Controle.canal_min
            else:
                self.canalAtual += 1
    
    def canal_menos(self):
        if self.ligado:
            if self.canalAtual == Controle.canal_min:
                self.canalAtual = Controle.canal_max
            else:
                self.canalAtual -= 1
        
    def volume_mais(self):
        if self.ligado:
            if self.volumeAtual == Controle.volume_max:
                pass
            else:
                self.volumeAtual += 1
    
    def volume_menos(self):
        if self.ligado:
            if self.volumeAtual == Controle.volume_min:
                pass
            else:
                self.volumeAtual -= 1
    
    def mostrar_tv(self):
        conteudo = ""
        if self.ligado == True:
            conteudo = f"Canal = "
            for c in range(Controle.canal_min, Controle.canal_max + 1):
                if c == self.canalAtual:
                    conteudo += f"[yellow on yellow] {c} [/]"
                else:
                    conteudo += f" {c} "
            conteudo += f"\nVolume = "
            for c in range(Controle.volume_min, Controle.volume_max + 1):
                if c <= self.volumeAtual:
                    conteudo += f"[green on green] . [/]".replace("."," ")
                else:
                    conteudo += f"[white on white] . [/]".replace("."," ")
        else:
            conteudo = f"[red]Tv Esta Desligada!!![/]"
            
        tv = Panel(conteudo, title="[TV]",width=50,style="green")
        print(tv)
        
        

        
        
c1 = Controle()
while True:
    c1.mostrar_tv()
    comando = str(input(" < CH > - VOL + : "))
    match comando:
        case "0":
            break
        case "@":
            c1.liga_desliga()
        case ">":
            c1.canal_mais()
        case "<":
            c1.canal_menos()
        case "-":
            c1.volume_menos()
        case "+":
            c1.volume_mais()
    print("\n"*12)