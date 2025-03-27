"""
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
"""

numero = int(input("Ingresa un número: "))
if numero < 2:
    print(f"{numero} no es primo")
elif numero in [2,3,5,7]:
    print(f"{numero} --> Es primo")
elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
    print(f"{numero} es primo")

print("\nNumeros primos\n")
for i in range(2,101):    
    # Se trata a 2,3,5,7 como primos
    if i in [2,3,5,7]:
        print(f"{i} --> Es primo")
    elif i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    print(f"{i} --> Es primo")
        
