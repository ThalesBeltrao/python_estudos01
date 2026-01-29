from math import sqrt
#def create_def(func):
    #def interna(*args, **kwargs):
        #for arg in args:
            #check_instance(arg)
        #resultado = func(*args, **kwargs)
        #return resultado
    #return interna


#def check_instance(arg):
        #if not isinstance(arg, int):
            #raise TypeError("Deve ser um numero inteiro")


#@create_def
#def soma(x, y):
   #return x + y


#resultado1 = create_def(soma)
#print(resultado1("5", "5"))


# Melhor a minha lógica de programaçao que esta péssima

def create_modify_sqrt(func):
    def interna(*args):
        receive_param = func(*args)
        for arg in args:
            check_param(arg)
            result_sqrt = sqrt(receive_param)
            return result_sqrt

    return interna


@create_modify_sqrt
def soma(x, y):
    print(f"{soma.__name__}")
    return x + y

def check_param(arg):
    if not isinstance(arg, (int, float)):
        raise TypeError("Precisa ser um numero(inteiro, flutuante) e não uma string")

resultado = soma("5", "5")
print(resultado)








