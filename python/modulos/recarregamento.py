import modulo_0
# recarregar o modulo
import importlib

print(modulo_0.nome)

# ele é apenas uma unica vez singleton como padrão
for i in range(3):
    importlib.reload(modulo_0)