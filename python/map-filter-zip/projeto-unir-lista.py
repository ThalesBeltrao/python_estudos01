# Projeto unir duas listas em ordem
# Criar uma funcao que recebe uma lista duas listas
# Faz a entrega das duas listas unidas
#  Usando a funcao zip

def join_list(*args):
    def excute_df():
        unir_list = zip(*args)
        return list(unir_list)
    return excute_df







#resultado = join_list(list_city, list_uf)
#print(resultado())

# Fazendo de maneira Vanilla Coding
list_city = ["Salvador", "Ubatuba", "Belo Horizonte"]
list_uf = ["BA", "SP", "MG"]


def unit_list(l1, l2):
    # Aqui Ele vai buscar o menor índice
    size_list = min(len(l1), len(l2))
    result = [(l1[i], l2[i]) for i in range(size_list)]
    return result



print(unit_list(list_city, list_uf))