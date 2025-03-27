"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""
alfabetoMorse = {
    "A" : ".—", "N" : "—.", "0" : "—————",
    "B" : "—...", "Ñ" : "——.——", "1" : ".————",
    "C" : "—.—.", "O" : "———", "2" : "..———",
    "CH" : "————", "P" : ".——.", "3" : "...——",
    "D" : "—..", "Q" : "——.—", "4" : "....—",
    "E" : ".", "R" : ".—.", "5" : ".....",
    "F" : "..—.", "S" : "...", "6" : "—....",
    "G" : "——.", "T" : "—", "7" : "——...",
    "H" : "....", "U" : "..—", "8" : "———..",
    "I" : "..", "V" : "...—", "9" : "————.",
    "J" : ".———", "W" : ".——", "." : ".—.—.—",
    "K" : "—.—", "X" : "—..—", "," : "——..——",
    "L" : ".—..", "Y" : "—.——", "?" : "..——..",
    "M" : "——", "Z" : "——..", "\"" : ".—..—.", "/" : "—..—."
}

morseAtexto = {v:k for k,v in alfabetoMorse.items()} # Invierte claves y valor del dict de alfabetoMorse

# Función texto a morse
def text_To_Morse(texto):
    for letra in texto:
        textoNuevo = alfabetoMorse.get(letra.upper(), letra)
        print( ''.join(textoNuevo), end=' ')

def Morse_To_text(texto):
    palabras = texto.split(' ')  # Dividimos las palabras por el espacio
    for palabra in palabras:
        for letra in palabra.split():
            palabraNueva = ''.join(morseAtexto.get(letra, '?') )
            print(palabraNueva, end=' ')  # Imprimimos la palabra nueva

def deteccion(texto):
    for caracter in texto.split():
        if (caracter in alfabetoMorse.values()):
            return Morse_To_text(texto)
        else:
            return text_To_Morse(texto)  

deteccion(".... ——— .—.. .—")

