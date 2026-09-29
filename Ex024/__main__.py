from arquivo import *
from rich import print, inspect
from rich.traceback import install
install()

def main():
    a1 = PDF('Prova', 250_000)
    abrir_arquivo(a1)

if __name__ == '__main__':
    main()