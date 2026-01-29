# * = __all__ você pode escolhar quais objetos  quer importar de uma vez do modulo
# __all__ = ["fala_oi", "nome"]




# def fala_oi(nome):
    #  print("oi", nome)


# nome = "Neymar "
try:
    from modulop import soma
except ModuleNotFoundError:
    print("vai dar erro porque o modulo ele esta sendo carregado em outra pasta")


