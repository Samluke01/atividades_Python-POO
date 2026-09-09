from Funcionarios import *
from rich import print
from rich.traceback import install

install()

def main():
    f1 = FuncionarioHorista('João',12, 200)
    f1.calc_sal()
    f1.analisar_sal()
    
    f2 = FuncionarioMensalista('Joey', 3500)
    f2.calc_sal()
    f2.analisar_sal()
if __name__ == '__main__':
    main()