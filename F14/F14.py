def media_aritmetica(lista):
    total_elementos = len(lista)
    suma_elementos = sum(lista)
    media = suma_elementos / total_elementos
    return media

# Ejemplo de uso:
lista_numeros = [int(x) for x in input("Ingrese los números separados por espacios: ").split()]
media_resultante = media_aritmetica(lista_numeros)
print("La media aritmética de la lista es:", media_resultante)