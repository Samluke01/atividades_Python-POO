from personagem import *
from rich.traceback import install
install()
def main():
    g1 = Guerreiro('Darth',20000)
    g2= Guerreiro('Eilort',20000)
    g1.atacar(g2,1456)
    g2.atacar(g1,1234)
    g1.curar()
    
if __name__ == '__main__':
    main()