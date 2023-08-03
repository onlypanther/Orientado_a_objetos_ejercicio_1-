def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma

# Ejemplo de uso:
lista_numeros = [int(x) for x in input("Ingrese los números separados por espacios: ").split()]
suma_total = calcular_suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)