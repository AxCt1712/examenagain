### evaluacion.py ###
from pila import Pila

# Evalúa una expresión en notación postfija (solo con números de un dígito)
def evaluar_postfija(expresion):
    pila = Pila()  # Pila para los operandos

    for simbolo in expresion:
        if simbolo.isdigit():
            pila.push(int(simbolo))  # Si es número, se apila
        elif simbolo in '+-*/^':
            op2 = pila.pop()  # Operando derecho
            op1 = pila.pop()  # Operando izquierdo
            # Se realiza la operación correspondiente
            if simbolo == '+': pila.push(op1 + op2)
            elif simbolo == '-': pila.push(op1 - op2)
            elif simbolo == '*': pila.push(op1 * op2)
            elif simbolo == '/': pila.push(op1 // op2)  # División entera
            elif simbolo == '^': pila.push(op1 ** op2)  # Potencia

    return pila.pop()  # Resultado final