def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso:
numero_dado = int(input("Ingrese un número: "))

if es_par(numero_dado):
    print(numero_dado, "es un número par.")
else:
    print(numero_dado, "es un número impar.")