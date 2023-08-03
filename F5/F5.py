def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Ejemplo de uso:
grados_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
print("La temperatura en grados Celsius es:", grados_celsius)