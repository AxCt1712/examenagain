### main.py ###
from menu import mostrar_menu, ejecutar_opcion

# Punto de entrada principal del programa
def main():
    opcion = ''
    while opcion != '3':  # Repite el menú hasta que el usuario elija salir
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)

if __name__ == '__main__':
    main()
