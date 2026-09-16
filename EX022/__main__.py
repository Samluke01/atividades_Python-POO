from aluno import *
from rich import print, inspect

def main():
    a1 = Aluno('Eduardo', 1999, 'ADS')
    a1.add_curso('MODA')
    a1.curso = 'MODA'
    
    inspect(a1,private=True,methods=True)
if __name__ == '__main__':
    main()