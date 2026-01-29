from itertools import count
import math as mt

from numpy.ma.core import around


def imposto(x:int):
    def calcular_imposto():
        if x <= 2000:
            print("Isento")
        elif 2000 <  x <= 3000:
           resultado_imposto =  x * 0.08
           print(f"valor do imposto: {resultado_imposto:.2f}")
        elif 3000 < x <= 4000:
            resultado_imposto = x * 0.18
            print(f"valor do imposto: {resultado_imposto:.2f}")
        elif x >= 4500:
            resultado_imposto = x * 0.28
            print(f"valor do imposto: {resultado_imposto:.2f}")

    return calcular_imposto


valor = imposto(2000)
valor()

