from validador import *
from rich import print, inspect
from rich.traceback import install
install()

def main():
    validador_dado(Email(),'lmkjf@gail.com')
    validador_dado(Usuario(),'Death_metal')
    validador_dado(Senha(),'Etilor2')
    
if __name__ == '__main__':
    main()