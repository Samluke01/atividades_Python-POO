from cafeteira import *
from rich import print, inspect
from rich.traceback import install
install()
def main():
    bebida = Leite()
    bebida.preparar()

if __name__ == '__main__':
    main()