def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: No se puede dividir entre cero."

# Ejemplo de uso:
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Suma:", suma(numero1, numero2))
print("Resta:", resta(numero1, numero2))
print("Multiplicación:", multiplicacion(numero1, numero2))
print("División:", division(numero1, numero2))