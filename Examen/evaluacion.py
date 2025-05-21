### evaluacion.py ###
from pila import Pila

def evaluar_postfija(expresion):
    pila = Pila()
    tokens = expresion.split()  # Entrada postfija con tokens separados por espacio

    try:
        for token in tokens:
            try:
                # Intenta convertir a número (soporta enteros grandes)
                num = int(token)
                pila.push(num)
            except ValueError:
                if token in '+-*/^':
                    op2 = pila.pop()
                    op1 = pila.pop()
                    if op1 is None or op2 is None:
                        raise ValueError("Expresión postfija inválida: operandos insuficientes")
                    # Realiza la operación y apila el resultado
                    if token == '+': pila.push(op1 + op2)
                    elif token == '-': pila.push(op1 - op2)
                    elif token == '*': pila.push(op1 * op2)
                    elif token == '/': pila.push(op1 // op2)
                    elif token == '^': pila.push(op1 ** op2)
                else:
                    raise ValueError(f"Símbolo no válido: '{token}'")

        resultado = pila.pop()
        if not pila.is_empty():
            raise ValueError("Expresión postfija inválida: operandos sobrantes")
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"