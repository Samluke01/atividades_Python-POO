from rich import print
class Funcionario:
    def __init__(self,nome="Anonimo",setor="Anonimo",cargo="Anonimo",empresa="Desconhecida"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa
        
    def apresentacao(self):
        return f":handshake: Ola, sou [yellow]{self.nome}[/], trabalho como [blue]{self.cargo}[/] no setor de [blue]{self.setor}[/] na empresa [green]{self.empresa}[/]"
    
    
f1=Funcionario("Gabriel","TI","Desenvolvedor Backend","Technix")
print(f1.apresentacao())