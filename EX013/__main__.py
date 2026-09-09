from rich.table import Table
from rich import print
from rich.traceback import install
from frete import *
install()

def main():
    dist = 46
    
    viagem = [Moto(dist),Caminhão(dist),Drone(dist)]
    
    table = Table(title='Tabela de frete', width=50)
    
    table.add_column('Distancia', justify='left')
    table.add_column('Tipo', justify='left')
    table.add_column('Frete', justify='left')
    
    table.add_row(f'{dist}Km','Moto',f'{viagem[0].calcular_frete()}')
    table.add_row(f'{dist}Km','Caminhão',f'{viagem[1].calcular_frete()}')
    table.add_row(f'{dist}Km','Drone',f'{viagem[2].calcular_frete()}')
    
    print(table)
    
if __name__ == '__main__':
    main()