from pagamento import *
from rich import print, inspect
from rich.traceback import install
install()

def main():
    finalizar_compra(Boleto(), 789465)

if __name__ == '__main__':
    main()