"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""

from datetime import datetime
import re

def validacionFecha(fecha):
    """
    Función que valida que las fehcas ingresadas tengan el formato dd/mm/yyyy
    """
    regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    return bool(re.match(regex, fecha))

def validacionFechaReal(fecha):
    """
    Función para validar que la fecha sea correcta, es decir, 
    si envio 31 de feb no acepta porque no existe
    """
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def calculoDias(cadFecha1, cadFecha2): # cadFecha1 and cadFecha2 son cadenas
    """
    Función para calcular días. 
    Recibe como parámetro dos cadenas de fechas y devuelve la cantidad de días entre esas dos fechas
    """
    try: 
        if not validacionFecha(cadFecha1) or not validacionFecha(cadFecha2):
            raise ValueError("Una o ambas fechas no tienen el formato correcto")
        
        if not validacionFechaReal(cadFecha1) or not validacionFechaReal(cadFecha2):
            raise ValueError("Una o ambas fehcas no son válidas")
        

        cadFecha1 = datetime.strptime(cadFecha1, "%d/%m/%Y")
        cadFecha2 = datetime.strptime(cadFecha2, "%d/%m/%Y")

        if cadFecha1 > cadFecha2:
            dias = cadFecha1 - cadFecha2
            print(f"Los días que hay entre {cadFecha1.strftime('%d/%m/%Y')} y {cadFecha2.strftime('%d/%m/%Y')} son {dias.days}")
        else: 
            dias = cadFecha2 - cadFecha1
            print(f"Los días que hay entre {cadFecha1.strftime('%d/%m/%Y')} y {cadFecha2.strftime('%d/%m/%Y')} son {dias.days}")

        return dias.days
    
    except ValueError:
        return ValueError

print(calculoDias("18/02/2002", "29/07/2001"))
