from funcionario import *

def main():
    f = Desenvolvedor('Pedro',1_800)
    f.salario = 2500
    print(f.calcular_bonus())

if __name__ == '__main__':
    main()