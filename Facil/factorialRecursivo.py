"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)
    
print(factorial(4))