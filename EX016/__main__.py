from rich import inspect
from termostato import *
def main():
    t = Termostato()
    try:
        t.temperatura = 25
    except Exception as e:
        print(f'Houve um erro: {e}')
    print(f'A Temperatura atual é {t.ftemperatura}')
    inspect(t,private=True,methods=True)
    

if __name__ == '__main__':
    main()