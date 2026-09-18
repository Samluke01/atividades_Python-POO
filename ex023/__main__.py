from funcionario import *

def main():
    f1 = Gerente('Pedro',1_800)
    f2 = Desenvolvedor('João',1_850)
    f3 = Designer('Amaro',1_862)
    f1.salario = 3000
    f2.salario = 2500
    f3.salario = 2300
    print(f1)
    print(f2)
    print(f3)

if __name__ == '__main__':
    main()