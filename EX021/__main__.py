from rich import print, inspect
from conta_bancaria import *

def main():
    print('Criando a Conta...')
    cc = ContaBancaria(1112,'Gabriel Barbosa',7000, 'death')
    inspect(cc,private=True,methods=True)
    cc.sacar(500,'123456')
    cc.depositar(1456)
    cc.nome = 'Emanuel'
if __name__ == '__main__':
    main()