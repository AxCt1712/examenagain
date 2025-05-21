### pila.py ###
# Clase que implementa una pila (estructura LIFO)
class Pila:
    def __init__(self):
        self.items = []  # Lista para almacenar los elementos de la pila

    def push(self, item):
        self.items.append(item)  # Agrega un elemento al tope de la pila

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remueve y devuelve el tope de la pila
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Devuelve el tope sin removerlo
        return None

    def is_empty(self):
        return len(self.items) == 0  # Verifica si la pila está vacía

    def clear(self):
        self.items = []  # Vacía completamente la pila

