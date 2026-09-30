class Produto:
    def __init__(self,nome:str,preço:float):
        self.nome = nome
        self.preço = preço
        
    def __str__(self):
        return f'{self.nome} ({FormataCedula(self.preço)})'
    
class Carrinho:
    def __init__(self,produtos:list=[]):
        self.produtos = produtos if produtos else []
    
    @property
    def total(self):
        return sum(p.preço for p in self.produtos)
    
    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError('Você tentou adicionar algo invalido ao carrinho')
        
    def __str__(self):
        conteudo = '-'*20
        for c in self.produtos:
            conteudo += f'\n{c}'
        conteudo += '\n'
        conteudo += '-'*20
        conteudo += f'\nTotal: {FormataCedula(self.total)}'
        return conteudo
    
def FormataCedula(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor,grouping=True,symbol=True)