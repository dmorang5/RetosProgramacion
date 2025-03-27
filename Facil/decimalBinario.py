"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""

numero = int(input("Ingrese un número: "))
binario = ""

# Decimal a binario
# 28 = 11100

while numero > 0:
    residuo = numero % 2
    binario = str(residuo) + binario
    numero = numero // 2
print(f"El binario del número{numero} es {binario}")