class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._area = None
        self._altura = None
        self._base = None
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self,valor):
        if valor <= 0:
            raise ValueError('Base com valor invalido!!!')
        else:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self,valor):
        if valor <= 0:
            raise ValueError('Altura com valor invalido!!!')
        else:
            self._altura = valor
    
    @property
    def medidas(self):
        return f'Base = {self._base} \nAltura = {self._altura} \nÁrea = {self.area}'
    
    @medidas.setter
    def medidas(self,tup):
        if type(tup[0]) == str or type(tup[1]) == str:
            raise SyntaxError('Erro: Os Valores de base e altura devem ser apenas numeros!!!')
        if tup[0] <= 0 or tup[1] <= 0:
            raise ValueError('Erro: Base ou Altura com valor invalido!!!')
        else:
            self._base = tup[0]
            self._altura = tup[1]
        
    
    @property
    def area(self):
        return self._base * self._altura
    

    