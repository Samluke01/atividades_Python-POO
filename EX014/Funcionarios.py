from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    def __init__(self,nome,sal_bruto,salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f'O Salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de R${self.salario:.2f} e corresponde a [yellow]{self.resp:.1f} salárioas mínimos.'
        print(Panel(conteudo,title='Análise de Salário',width=50))
    
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valorHora, horasTrab, sal_bruto=0, salario=0):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valorHora
        self.horas_trab = horasTrab
        
    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab
        self.salario = self.salario - (self.salario * (self.inss / 100))
        self.resp = self.salario / self.sal_min
    
class FuncionarioMensalista(Funcionario):
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        self.resp = self.salario / self.sal_min