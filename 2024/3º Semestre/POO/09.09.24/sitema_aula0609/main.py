from cliente import Cliente
from vendedor import Vendedor

# MAIN
list_vendedores = list()
carlos = Vendedor(n='Carlos', cpf='000000', t='000000', mat='000000', sal='3200')
antonio = Cliente(n='Antonio', cpf='111111', t='111111', num_fidel='111111')

print('===== Antes =====')
print(carlos.get_pontos())
print(antonio.get_credito())

carlos.gerar_valores()
antonio.gerar_valores()

print('===== Depois =====')
print(carlos.get_pontos())
print(antonio.get_credito())
