import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Ejemplo de uso:
radio_del_circulo = float(input("Ingrese el radio del círculo: "))
area_del_circulo = calcular_area_circulo(radio_del_circulo)
print("El área del círculo es:", area_del_circulo)