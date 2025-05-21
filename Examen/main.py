    ### main.py ###
from menu import mostrar_menu, ejecutar_opcion

# Función principal del programa
def main():
    opcion = ''
    while opcion != '3':
        mostrar_menu()  # Mostrar menú de opciones
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)  # Ejecutar la opción seleccionada

if __name__ == '__main__':
    main()  # Punto de entrada del programa