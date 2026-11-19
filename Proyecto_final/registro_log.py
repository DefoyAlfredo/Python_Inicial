from datetime import datetime
from config import LOG_PATH

def registrar_evento(nivel: str, mensaje: str):
    # Registra eventos y errores en el archivo de log local.
    
    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] [{nivel.upper()}] {mensaje}\n"
    try: 
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(linea)
    except Exception as e:
        print(f"Error al escribir el log: {e}")
        