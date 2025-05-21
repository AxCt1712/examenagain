 ### conversion.py ###
from pila import Pila

  # Prioridad de operadores (de mayor a menor)
precedencia = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

  # Verifica si un símbolo es un operador válido
def es_operador(simbolo):
      return simbolo in '+-*/^'

  # Valida que la expresión sea una infija simple con operandos y operadores alternados
def es_infija_valida(expresion):
      simbolos = list(expresion.replace(' ', ''))
      parentesis = 0
      ultimo = ''

      for simbolo in simbolos:
          if simbolo == '(':
              parentesis += 1
          elif simbolo == ')':
              parentesis -= 1
              if parentesis < 0:
                  return False
          elif simbolo.isalnum():
              if ultimo.isalnum():
                  return False
          elif es_operador(simbolo):
              if ultimo in ('', '(', '+', '-', '*', '/', '^'):
                  return False
          else:
              return False
          ultimo = simbolo

      return parentesis == 0 and ultimo not in '+-*/^('

  # Convierte una expresión infija a postfija (con validación)
def infija_a_postfija(expresion):
      if not es_infija_valida(expresion):
          return "Error: solo se permiten expresiones infijas como '2+2', '1/2+3*2', etc."

      pila = Pila()
      salida = []
      simbolos = list(expresion.replace(' ', ''))

      for simbolo in simbolos:
          if simbolo.isalnum():
              salida.append(simbolo)
          elif simbolo == '(':
              pila.push(simbolo)
          elif simbolo == ')':
              while not pila.is_empty() and pila.peek() != '(':
                  salida.append(pila.pop())
              pila.pop()
          elif es_operador(simbolo):
              while (not pila.is_empty() and pila.peek() != '(' and
                     precedencia.get(simbolo, 0) <= precedencia.get(pila.peek(), 0)):
                  salida.append(pila.pop())
              pila.push(simbolo)

      while not pila.is_empty():
          salida.append(pila.pop())

      return ''.join(salida)
