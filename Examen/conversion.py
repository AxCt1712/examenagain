### conversion.py ###
from pila import Pila

# Prioridad de operadores (de mayor a menor)
precedencia = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

# Verifica si un símbolo es un operador válido
def es_operador(simbolo):
    return simbolo in '+-*/^'

# Convierte una expresión en notación infija a notación postfija (RPN)
def infija_a_postfija(expresion):
    pila = Pila()  # Pila para operadores
    salida = []    # Lista para la expresión en postfijo
    simbolos = list(expresion.replace(' ', ''))  # Elimina espacios y separa en símbolos

    for simbolo in simbolos:
        if simbolo.isalnum():
            salida.append(simbolo)  # Si es operando, va directo a la salida
        elif simbolo == '(':
            pila.push(simbolo)  # Abre paréntesis: se guarda en la pila
        elif simbolo == ')':
            # Cierra paréntesis: desapilar hasta encontrar '('
            while not pila.is_empty() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  # Elimina el '('
        elif es_operador(simbolo):
            # Manejo de precedencia de operadores
            while (not pila.is_empty() and pila.peek() != '(' and
                   precedencia.get(simbolo, 0) <= precedencia.get(pila.peek(), 0)):
                salida.append(pila.pop())
            pila.push(simbolo)  # Coloca el operador en la pila

    # Al final, vacía la pila en la salida
    while not pila.is_empty():
        salida.append(pila.pop())

    return ''.join(salida)