"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def esAnagrama(palabra1, palabra2):
    letras1 = sorted(list(palabra1.lower()))
    letras2 =  sorted(list(palabra2.lower()))

    if palabra1.lower() == palabra2.lower(): 
        return False
    
    elif letras1 == letras2:
        return True
    
    else:
        return False

print(esAnagrama("amor", "roma")) 
