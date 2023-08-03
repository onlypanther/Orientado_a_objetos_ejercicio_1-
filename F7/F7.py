def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# Ejemplo de uso:
lista_numeros = [int(x) for x in input("Ingrese los números separados por espacios: ").split()]
maximo_numero, minimo_numero = encontrar_maximo_minimo(lista_numeros)
print("El número más grande es:", maximo_numero)
print("El número más pequeño es:", minimo_numero)