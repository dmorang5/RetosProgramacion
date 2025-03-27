"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def enMayuscula(cadena):
    palabras = cadena.split()

    mayusculas = []
    for palabra in palabras:
        if len(palabra) > 0:
            mayuscula = palabra[0].upper() +palabra[1:].lower()
            mayusculas.append(mayuscula)

    return ' '.join(mayusculas)

print(enMayuscula("hola mundo"))