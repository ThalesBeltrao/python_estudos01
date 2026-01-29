
lista = [10, 20, 30, 40]

modificar = list(map(lambda x: x *2, lista))
print(modificar)

modificar_listcompreension = [n*2 for n in lista]
print(modificar_listcompreension)

###### filtro
filtrar = list(filter(lambda x: x>20, modificar_listcompreension))
print(filtrar)

filtrar_listcompreension = ...