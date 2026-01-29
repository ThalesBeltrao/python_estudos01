# Para medir a velocidade de execução de uma funcao
import time


# Agora criar uma funcão que tem um parametro
# Esse parametro ele faz com que a funcao possa ser modificada
# Conforme o seu Estado


def funcao_estado(detalhe=True):
    def recebe_funcao(func):
        def interna(*args, **kwargs):
            # Aqui é quando vai passar a execução da funcao
            inicio = time.time()
            tarefa = func(*args, **kwargs)
            fim = time.time()

            if detalhe:
                print(f"Funcao: {func.__name__} executada em , {fim - inicio:.6f}")

            else:
                print(f"Funcao: {func.__name__} executada em, {fim - inicio:.6f}")
            return tarefa
        return interna
    return recebe_funcao


@funcao_estado(detalhe=True)
def task_flash():
    time.sleep(1)
    return "Finalizado!"


@funcao_estado(detalhe=False)
def quick_task():
    time.sleep(0.5)
    return "feito"


task_flash()
