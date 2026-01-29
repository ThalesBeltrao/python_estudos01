# O interator é como se fosse um
# Copo cheio de bolinhas ele você pegasse um de cada vez



class Contador:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    # O __iter__ retorna ele mesmo
    def __iter__(self):
        return self

    def __next__(self):

        if self.inicio > self.fim:
            raise StopIteration ("Passou do limite")
        valor = self.inicio
        self.inicio += 1

        return valor


contador = Contador(1, 4)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
