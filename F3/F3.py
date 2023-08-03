import random

def generar_lista_aleatoria(longitud, minimo, maximo):
    lista_aleatoria = [random.randint(minimo, maximo) for _ in range(longitud)]
    return lista_aleatoria

# Ejemplo de uso:
longitud_lista = int(input("Ingrese la longitud de la lista: "))
valor_minimo = int(input("Ingrese el valor mínimo: "))
valor_maximo = int(input("Ingrese el valor máximo: "))

lista_aleatoria = generar_lista_aleatoria(longitud_lista, valor_minimo, valor_maximo)
print("Lista de números aleatorios:", lista_aleatoria)