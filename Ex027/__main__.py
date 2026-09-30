from compras import *
from rich import print, inspect
from rich.traceback import install
from rich.panel import Panel


def main():
    p1 = Produto('Caderno', 32.65)
    p2 = Produto('Caneta', 8.50)
    p3 = Produto('Mochila', 430.44)
    p4 = Produto('Estojo', 85.38)
    
    c1 = Carrinho()
    
    c1 = c1 + p1 + p3 +p4
    inspect(c1)
    print(c1)
    
if __name__ == '__main__':
    main()