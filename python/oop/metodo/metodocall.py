# Método especial __cal__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a intancia de uma classe "callable"


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print("Chamando o telefone")


call1 = CallMe("129914807061")
print(call1.phone)
call1()  # CallMe' object is not callable ( ele não é executável)


# metodo call faz a instancia ser executavel 