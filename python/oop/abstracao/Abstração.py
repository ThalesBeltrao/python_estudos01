# Classes Abstratas -Abstract Base Class
# São usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criatem métodos concretos. tambem pode ter
# métodos concretos por elas mesmas
# @abstractemethods são metos que não tem corpo
# abstratos é porque elas não podem ser instanciadas
# diretamete
# métodos abstratos devem ser implementados
# nas subclasses (@abastractmethod)
#uma classe abstrata em python tem suas metclasse
# sendo ABCmeta
# È possívek criar @property @setter @classmethod
# @staticmethod e method como abstratos, para sso
# use @abstractmethod como decorator mais interno

from abc import ABC, abstractclassmethod


class Log(ABC):
    @abstractclassmethod
    def _log(self, msg):
        ...        #raise NotImplementedError("Implementar o metodo")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"sucess: {msg}")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


l = LogPrintMixin()
l.log_error("oi")



#  para ela ser abstrata ela precissa herdar o classe ABC e ter um metodo como abstrato

