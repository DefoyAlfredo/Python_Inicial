from colores import mostrar_error
# Funciones para validar entradas del usaurio por terminal
def leer_entero(mensaje: str) -> int:
    # Lee y valida un numero entero.
    while True: 
        try:
           return int(input(mensaje))
        except ValueError:
            mostrar_error("Entrada inválida. debe ingresar un número entero. ")

def leer_real(mensaje: str) -> float:
    #Lee y valida un numero flotante 
    while True:  
        try: 
            return float(input(mensaje))
        except valueError:
            mostrar_error("Entrada inválida. Debe ingresar un numero decimal. ")

def leer_texto(mensaje: str) -> str:
    #Lee un texxto asegurandose de que no este vacio.
    while True:  
        texto = input(mensaje).strip()
        if texto:
            return texto
        mostrar_error("El campo no puede estar vacío")
        
    
