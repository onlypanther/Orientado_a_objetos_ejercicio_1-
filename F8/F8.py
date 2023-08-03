def invertir_lista(lista):
    lista.reverse()

# Ejemplo de uso:
lista_numeros = [int(x) for x in input("Ingrese los números separados por espacios: ").split()]
invertir_lista(lista_numeros)
print("Lista invertida:", lista_numeros)