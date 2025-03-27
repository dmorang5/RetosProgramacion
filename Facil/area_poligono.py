"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

def areaPoligono(poligono): #poligono será dicc que contendrá tipo, base, altura
    """
    Función para calcular el área de polígono. 
    Se podrá calcular el área de tres tipos y cada tipo tendrá campos únicos. 
        Triangulo: base y altura
        Cuadrado: lado
        Rectangulo: largo y ancho
    """    

    tipo = poligono["tipo"]

    if tipo == "triangulo":
        base = poligono["base"]
        altura = poligono["altura"]
        area = base * altura / 2
        print(f"El área del {poligono["tipo"]} es {area}")

    elif tipo == "cuadrado":
        lado = poligono["lado"]
        area = lado ** 2
        print(f"El área del {poligono["tipo"]} es {area}")

    elif tipo == "rectangulo":
        largo = poligono["largo"]
        ancho = poligono["ancho"]
        area = largo * ancho
        print(f"El área del {poligono["tipo"]} es {area}")
    else:
        print("Polígono no disponible")

areaPoligono({"tipo": "triangulo", "base": 5, "altura": 10})
areaPoligono({"tipo": "cuadrado", "lado": 4})
areaPoligono({"tipo": "rectangulo", "largo": 8, "ancho": 6})