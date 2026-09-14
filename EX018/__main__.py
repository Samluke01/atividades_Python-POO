from credencial import Credencial
from rich import inspect, print

def main():
    c = Credencial()
    try:
        c.senha = 'angra'
    except Exception as e:
        print(f'[red]Erro: {e}[/]')
    inspect(c,private=True,methods=True)
    print(c.validar('angra'))

if __name__ == '__main__':
    main()