# dir, hasattr e getattr em Python

string = "luiz"
metodo = "upper"

if hasattr(metodo, "upper"):
    print(True)

# pode ser de forma dinamica
print()
if hasattr(string, metodo):
    print(True)
    print(string.upper())

# getattr ele chama criaatr
# executa uma variavel como se fosse um metodo
print()
print(getattr(string, metodo)())
