"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""

def esArmstrong(numero):
    digitos = len(numero)
    # print(f"El número tiene {digitos} digitos")
    # print(f"El número ingresado es {numero}")

    suma = 0
    for num in numero:
        res = int(num) ** digitos
        suma = suma + res
    # print(f"La sumatoria de todos los resultados de la potencia de cada digito es {suma}")

    if suma == int(numero):
        return True
    else:
        return False

print(esArmstrong('9474'))