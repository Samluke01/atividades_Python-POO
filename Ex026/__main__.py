from mensagem import *
from rich import print, inspect
from rich.traceback import install
install()

def main():
    Alerta("Ola. Gafanhoto!").mostrar()
    
if __name__ == '__main__':
    main()