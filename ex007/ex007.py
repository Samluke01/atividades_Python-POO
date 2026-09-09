from rich import print
'''
class Livro:
    def __init__(self,titulo,pag):
        self.titulo = titulo
        self.pag = pag 
        self.pag_atual = 1
        
    def avancar(self,num):
        cont = 0
        for c in range(0, num, 1):
            if not self.fim():
                self.pag_atual += 1
                print(f"Pagina {self.pag_atual} :arrow_forward:", end=' ')
                cont += 1 
        print(f"Você passou {cont} Paginas e agora esta na pagina {self.pag_atual}")
        if self.fim():
            print(f"Você Chegou ao final do livro")


    def fim(self):
        return True if self.pag_atual == self.pag else False            
'''    

class Livro:
    def __init__(self,titulo,pag):
        self.titulo = titulo
        self.pag = pag 
        self.pag_atual = 1
        
    def avancar(self,num):
        cont = 0
        for c in range(0, num, 1):
            if self.pag_atual != self.pag:
                self.pag_atual += 1
                print(f"Pagina {self.pag_atual} :arrow_forward:", end=' ')
                cont += 1 
        print(f"Você passou {cont} Paginas e agora esta na pagina {self.pag_atual}")
        if self.pag_atual == self.pag:
            print(f"Você Chegou ao final do livro")
  




c1 = Livro("Abc", 15)
c1.avancar(4)
c1.avancar(5)
c1.avancar(8)


