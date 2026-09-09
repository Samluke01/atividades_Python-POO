from rich import print
from deep_translator import GoogleTranslator

class Caneta:
    def __init__(self,cor):
        self.cor = cor 
        self.trad = GoogleTranslator(source="pt", target="en").translate(self.cor).lower()
    
    
    def destampar(self):
        self.destampar = True
    
    
    def escrever(self,frase):
        if self.destampar == True:
            print(f"[{self.trad}]{frase}[/]")
        else:
            print(frase)
            
    
    def quebrar_linha(self,num):
        for c in range(0,num,1):
            print(" ")
            
            
c1=Caneta('Azul')
c2=Caneta('Verde')
c3=Caneta('Amarelo')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Nois é top")
c1.quebrar_linha(2)
c2.escrever("Ai vamos nós")
c3.escrever("Ai sim")