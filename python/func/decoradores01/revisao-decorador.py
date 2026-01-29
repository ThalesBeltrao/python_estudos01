# Função dos Decoradores
# Modificar, Restringir, Adicionar


def saudacao_decorador(fun):

    def intern(nome):
        print("Estou te decorando")
        fun(nome)
        print("Te decorei")

    return intern

@saudacao_decorador
def saudacao(nome):
    print(f"Meu nome é {nome}")


# Decoradores com multiplos argumentos

def decorador_generico(func):
    def interna(*args, **kwargs):
        print(f"Chamando {func.__name__}, com os agumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        print("Execução Finalizada")
        return resultado
    return interna


@decorador_generico
def soma(a, b):
    return a + b


print(soma(3, 4))
print()

# decoradores aninhados

def decorador1(func):
    def interna1(*args, **kwargs):
        print("Ainda não fui decorado pelo decorador1")
        resultado = func(*args, **kwargs)
        print("Agora fui decorado pelo decorador1")
        return resultado
    return interna1


def decorador2(func):
    def interna(*args, **kwargs):
        print("Ainda não fui decorado pelo decorador2")
        resultado = func(*args, **kwargs)
        print("Agora fui decorado pelo decorador2")

        return resultado

    return interna

@decorador2
@decorador1
def multiplica(x, y):
    print(x * y)


multiplica(2, 3)

