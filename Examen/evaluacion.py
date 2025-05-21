### evaluacion.py ###
from pila import Pila

# Evalúa una expresión en postfijo (solo números enteros positivos de un dígito)
def evaluar_postfija(expresion):
    pila = Pila()

    try:
        for simbolo in expresion:
            if simbolo.isdigit():
                pila.push(int(simbolo))
            elif simbolo in '+-*/^':
                op2 = pila.pop()
                op1 = pila.pop()
                if op1 is None or op2 is None:
                    raise ValueError("Expresión postfija inválida: operandos insuficientes")
                if simbolo == '+': pila.push(op1 + op2)
                elif simbolo == '-': pila.push(op1 - op2)
                elif simbolo == '*': pila.push(op1 * op2)
                elif simbolo == '/': pila.push(op1 // op2)
                elif simbolo == '^': pila.push(op1 ** op2)
            else:
                raise ValueError(f"Símbolo no válido en expresión postfija: '{simbolo}'")

        resultado = pila.pop()
        if not pila.is_empty():
            raise ValueError("Expresión postfija inválida: demasiados operandos")
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"