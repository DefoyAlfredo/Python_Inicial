from colorama import Fore, Style, init

#Inicializar colorama 
init(autoreset=True)

#Definicion de funciones para mensajes con colores.

def mostrar_exito(mensaje: str):
    print(f"{Fore.GREEN}[✔] {mensaje}{Style.RESET_ALL}")

def mostrar_error(mensaje: str):
    print(f"{Fore.RED}[X] {mensaje}{Style.RESET_ALL}")

def mostrar_advertencia(mensaje: str):
    print(f"Fore.YELLOW[⚠] {mensaje}{Style.RESET_ALL}")

def mostrar_info(mensaje: str):
    print(f"{Fore.CYAN}[i] {mensaje}{Style.RESET_ALL}")

def titulo(texto: str):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}=== {texto.upper()}==={Style.RESET_ALL}")
      