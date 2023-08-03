def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

# Ejemplo de uso:
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz_numeros = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz_numeros.append(fila)

print("\nMatriz generada:")
imprimir_matriz(matriz_numeros)