from abc import ABC
from datetime import date as dt

class Pessoa(ABC):
    def __init__(self,nome,nascimento):
        self._nome = nome
        self._nascimento = nascimento
        
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento):
        if nascimento < dt.today().year - 100 or nascimento > dt.today().year:
            raise ValueError(f'Ano {nascimento} invalido')
        else:
            self._nascimento = nascimento
    
    @property   
    def idade(self):
        return dt.today().year - self.nascimento
    
    @idade.setter
    def idade(self,valor):
        raise PermissionError('Você não pode alterar a idade. Mude o ano de nascimento!')
       
class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADM','ADS','ENG','CONT']
        self.curso = curso
        self._curso = curso
        
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self,curso):
        if curso not in self.cursos_oficiais:
            raise ValueError(f'O curso {curso} não está na lista de Cursos Oficiais.')
        else:
            self._curso = curso 
        
    def add_curso(self,curso):
        if 3 <= len(curso) <= 4:
            self.cursos_oficiais.append(curso)
        else:
            raise PermissionError('A Sigla do curso deve ter de 3 a 4 Caracteres!')