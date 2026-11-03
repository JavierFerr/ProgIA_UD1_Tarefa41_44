# Escribe unha función que reciba coma parámetros unha lista e mais unha función,
# e devolva unha nova lista onde cada elemento é o resultado de aplicares a función ao elemento orixinal da lista.

# Xera os test unitarios.

def calculos(lista, fun):
    sumando = input("Introduce un numero para sumar\n")

    print(f"Sumando {sumando} a los valores de la lista \n")
    listasum = []
    for num in lista:
        listasum.append(fun(num, sumando))
    print(listasum)

def suma(num,sumando):
    return num + 1

lista = [1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    
    calculos(lista,suma)