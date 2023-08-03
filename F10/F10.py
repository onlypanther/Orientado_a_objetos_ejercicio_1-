def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Ejemplo de uso:
numero_dado = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial_recursivo(numero_dado)
print("El factorial de", numero_dado, "es:", resultado_factorial)