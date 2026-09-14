from diario import Diario
from rich import print, inspect

def main():
    d = Diario()
    d.senha = 'Angra'
    
    d.escrever('Primeira mensagem')
    d.escrever('Lamb Of God')
    d.escrever('Iron Maiden')
    d.escrever('Angra')
    try:
        d.ler('Angra')
    except Exception as e:
        print(f'[red]Erro: {e}')
    inspect(d,private=True)


if __name__ == '__main__':
    main()