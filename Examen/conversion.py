### conversion.py ###
from pila import Pila
import re

# Diccionario con la precedencia de los operadores
precedencia = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

# Verifica si un símbolo es un operador aritmético
def es_operador(simbolo):
    return simbolo in '+-*/^'

# Divide la expresión en tokens: números, variables, operadores y paréntesis
def obtener_tokens(expresion):
    return re.findall(r'\d+|[a-zA-Z]+|[+\-*/^()]', expresion.replace(' ', ''))

# Valida que los tokens tengan una estructura de expresión infija correcta
def es_infija_valida(tokens):
    parentesis = 0
    ultimo = ''

    for token in tokens:
        if token == '(':
            parentesis += 1
        elif token == ')':
            parentesis -= 1
            if parentesis < 0:
                return False  # más paréntesis de cierre que de apertura
        elif token.isalnum():
            pass  # operandos válidos (números o letras)
        elif es_operador(token):
            if ultimo in ('', '(', '+', '-', '*', '/', '^'):
                return False  # operador mal ubicado
        else:
            return False  # token inválido
        ultimo = token

    return parentesis == 0 and ultimo not in '+-*/^('  # expresión válida si termina correctamente

# Convierte una expresión infija válida a postfija usando una pila
def infija_a_postfija(expresion):
    tokens = obtener_tokens(expresion)

    if not es_infija_valida(tokens):
        return "Error: solo se permiten expresiones infijas como '2+2', '1/2+3*2', etc."

    pila = Pila()
    salida = []

    for token in tokens:
        if token.isalnum():
            salida.append(token)  # Los operandos van directo a la salida
        elif token == '(':
            pila.push(token)  # Paréntesis de apertura va a la pila
        elif token == ')':
            # Extrae de la pila hasta encontrar el paréntesis de apertura
            while not pila.is_empty() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  # Elimina el '('
        elif es_operador(token):
            # Respeta precedencia de operadores al apilar
            while (not pila.is_empty() and pila.peek() != '(' and
                   precedencia.get(token, 0) <= precedencia.get(pila.peek(), 0)):
                salida.append(pila.pop())
            pila.push(token)

    # Vacia el resto de la pila al final
    while not pila.is_empty():
        salida.append(pila.pop())

    return ' '.join(salida)  # Devuelve la expresión postfija separada por espacios
