# Xera test uniatarios, primeiro para a función que calcula a area do circulo, e logo para o volume do cilindro.

import math

def areaCir(r):
    return math.pi * r**2

def volumCil(r,h):
    return areaCir(r)* h

if __name__ == '__main__':

    print("Introduzca o radio e altura do cilindro (cm)")
    r,h = float(input()),float(input())
    print(f"O volume e de {volumCil(r,h)} cm2")