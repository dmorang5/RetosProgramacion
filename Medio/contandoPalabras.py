"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""
import tabulate

frase = input("Ingrese una frase: ").lower()

signos_puntuacion = ".,;:!?¡¿()[]{}\"'"

frase_limpia = ""

# Limpieza de frase
for letra in frase:
    if letra not in signos_puntuacion:
        frase_limpia += letra

# Division de palabras
palabras = frase_limpia.split()

# Conteo de palabras
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] +=1
    else:
        conteo[palabra] = 1


#print(f"Las palabras de la frase ingresada {frase} son: {palabras}")
#print(f"La frase limpia de la frase ingresada es: {frase_limpia}")

print("El conteo de palabras de la frase es:")
print(f"{'Palabra':<10} {'Conteo'}")
print("-" * 20)
for palabra, cantidad in conteo.items():
    print(f"{palabra:<10} {cantidad}")
