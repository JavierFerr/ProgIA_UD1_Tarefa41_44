#Similar a exercicios anteriores, podes copiar o feito nesa parte e continuar ampliando:

# Escribir un programa que lea un enteiro positivo, n,
# introducido polo usuario e despois mostre en pantalla a suma de todos vos enteiros desde 1 ata n.

# Para facelo implementa unha función que reciba un valor n e calcule ou resultado usando a seguinte formula:

# resultado =  n * ( n + 1)  / 2

# Xera os test unitarios para a función feita. Chequea por exemplo, algun número do que sepas a solución,
# que ocorre cando lle pasas un número negativo… corrixe a partires do resultado do test o necesario para que saia todo ben.

def calcular_suma(n):
    if n < 0:
        return None
    return n * (n + 1) // 2

if __name__ == '__main__':

    n = int(input("Introduce un número entero positivo: "))

    resultado = calcular_suma(n)
    
    if resultado is None:
        print("Por favor, introduce un número positivo.")
    else:
        print(f"La suma de todos los enteros desde 1 hasta {n} es: {resultado}")