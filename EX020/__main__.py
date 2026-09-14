from retangulo import *
from rich import print, inspect

def main():
    r = Retangulo(7,4)
    

    inspect(r, private=True, methods=True)
    
    print(r.medidas)
if __name__ == '__main__':
    main()