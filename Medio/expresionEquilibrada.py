"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cierran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""
def verificacionBalance(expresion):
    stack = []
    signos = {')': '(', '}': '{', ']': '['}
    
    for caracter in expresion:
        if caracter in signos.values():
            stack.append(caracter)
        elif caracter in signos.keys():
            if stack and stack[-1] == signos[caracter]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(verificacionBalance("{ [ a * ( c + d ) ] - 5 }"))  # True
print(verificacionBalance("{ a * ( c + d ) ] - 5 }"))  # False
