from poligono import *
from rich.traceback import install
from rich import print, inspect
install()

def main():
    p1 = Quadrado(20)
    
    print(f'Perimetro = [green]{p1.perimetro():.1f}')
    print(f'Area = [green]{p1.area():.1f}')

if __name__ == '__main__':
    main()