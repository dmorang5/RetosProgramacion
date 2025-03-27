"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def cadenas(cadena1, cadena2):
    caracteresCadena1 = list(cadena1)
    caracteresCadena2 = list(cadena2)

    cadSalida1 = ""
    cadSalida2 = ""

    for caracterCad1 in caracteresCadena1:
        if caracterCad1 not in caracteresCadena2:
            cadSalida1 += caracterCad1

    for caracterCad2 in caracteresCadena2:
        if caracterCad2 not in caracteresCadena1:
            cadSalida2 += caracterCad2

    return cadSalida1, cadSalida2
    #print(f"Los caracteres de la cadena 1 son: {cadSalida1} y los de la cadena 2 son: {cadSalida2}")

print(cadenas("hola", "cama"))
