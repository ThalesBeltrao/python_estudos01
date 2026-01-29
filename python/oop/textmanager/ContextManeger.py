# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho = caminho_arquivo
        self.modo = modo  # modo whiter, read,
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.caminho, self.modo, encoding="UTF-8")
        return self._arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._arquivo.close()


a = MyContextManager("aula130.txt", "w", )

with a as arquivo:
    arquivo.write("thales willian \n")
    arquivo.write("Julia Silva \n")
    print(arquivo)

"""Context manager abrir e fechar
conectar e desconectar
capturar e descapiturar """


# Exception em context manager com classes
# tratar exceção


class MyOpen:
    def __init__(self, caminho, modo):  # caminho é onde o arquivo se encontra e o modo qual tipo se vai whiter ou read
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None  # porque pode ser qualquer arquivo vai definir no enter o tipo de arquivo

    def __enter__(self):
        self._arquivo = open("contextmaneger02", "w", encoding="UTF-8")
        return self._arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._arquivo.close()

        # raise exc_type("Minha mensagem")

        # print(exc_type)  # tipo do erro nesse caso é TypeError
        # print(exc_val)  # qual o problema ocorreu
        # print(exc_tb) # tracebacck
        # return True # tratei a exceção de alguma maneira


# MyOpen("contextmaneger", "w") as arquivo:
# arquivo.write("tratando sobre exceções")


# context Manager com funcao - Criando e Usando Gerenciador de contexto


from contextlib import contextmanager


@contextmanager  # funcao decoradora
def my_open(caminho, modo):
    try:
        print("abrindo arquivo")
        arquivo = open(caminho, modo, encoding="UTF-8")
        yield arquivo
    except Exception as e:
        print("Ocorreu um erro", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()


with my_open("arquivo150", "w") as arq1:
    arq1.write("funcao decoradora",123)
