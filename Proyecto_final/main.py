from base_datos import inicializar_base_datos
from menu import mostrar_menu

def main():
    # Inicializar la bse de datos al arrancar 11

    inicializar_base_datos()
    # Lanzar el menú principal de la interfaz
    mostrar_menu()
    
if __name__ == "__main__":
    main()
    