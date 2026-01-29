def executa(func): # define Primeiro a funçaõ executa
    print("recebi a função")
    def interna(*args): # aqui recebe o valores da função soma que no caso é uma tupla
        for arg in args:
            analisar_dado(arg)
        v = func(*args) # Aqui é salvo o valor do return sum(*args) da funçao soma
        return v * 2
    return interna

def analisar_dado(args): # Define em Segundo a função analisar_dados
        if not isinstance(args, int):
            raise TypeError("Precisa ser um numero Inteiro")

@executa # decora a função soma
def soma(*args): # define a função soma
    return sum(args)

print(soma(5,2))


