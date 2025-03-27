"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

cadena = input("Ingrese una palabra o frase: ")

# Sin función del legunaje
cadenaLista = list(cadena)
#print(cadenaLista)

cadenaInvertida = ""
for letra in cadenaLista[::-1]:
    cadenaInvertida += letra

print(f"La palabra o frase ingresada es: {cadena}")
print(f"La palabra o frase invertida es: {cadenaInvertida}")

# Con función del lenguaje
#cadena_invertida = reversed(cadena)
#print("".join(reversed(cadena)))
