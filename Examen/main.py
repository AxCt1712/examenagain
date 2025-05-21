### main.py ###
from menu import mostrar_menu, ejecutar_opcion

def main():
    opcion = ''
    while opcion != '3':
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)

if __name__ == '__main__':
    main()