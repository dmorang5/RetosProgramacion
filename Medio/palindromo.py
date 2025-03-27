"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""

def limpieza(texto):
    signos_puntuacion = ".,;:!?¡¿()[]{}\"' "
    frase_limpia = ""

    for letra in texto:
        if letra not in signos_puntuacion:
            frase_limpia += letra
    return frase_limpia

def esPalindromo(texto):
    texto_limpio = limpieza(texto)
    
    texto = texto_limpio
    palindromo = ""


    for letra in texto:
        palindromo = letra + palindromo
    
    if palindromo == texto:
        return True
    else: 
        return False

print(esPalindromo("ana lleva al oso la avellana1"))
print(esPalindromo("ana lleva al oso la avellana"))