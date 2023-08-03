def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para hacer la comparación sin considerar mayúsculas o espacios
    cadena_limpia = cadena.replace(" ", "").lower()
    # Invertir la cadena
    cadena_invertida = cadena_limpia[::-1]
    # Comparar la cadena original con la cadena invertida
    return cadena_limpia == cadena_invertida

# Ejemplo de uso:
cadena_usuario = input("Ingrese una cadena de texto: ")
if es_palindromo(cadena_usuario):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")