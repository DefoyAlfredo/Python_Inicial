import subprocess
import sys


def asegurar_dependencias():
    """Verifica e instala 'colorama' si no está disponible en el entorno."""
    try:
        import colorama  # noqa: F401
    except ImportError:
        print("[!] 'colorama' no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])


asegurar_dependencias()


from base_datos import inicializar_base_datos
from menu import mostrar_menu

def main():
    # Inicializar la bse de datos al arrancar 11

    inicializar_base_datos()
    # Lanzar el menú principal de la interfaz
    mostrar_menu()
    
if __name__ == "__main__":
    main()
    