import sqlite3
from config import DB_PATH
from registro_log import registrar_evento


def  obtener_conexion():
    # establece y devuelve una conexion a la base de datos SQLite.
    
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row #perimte acceder a la columna por el nombre
    return conexion

def inicializar_base_datos():
    #Crear la tabla productos si no existe 
    try: 
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS productos (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nombre TEXT NOT NULL,
                               descripcion TEXT,
                               cantidad INTEGER NOT NULL,
                               precio REAL NOT NULL,
                               categoria TEXT
                            )
            """)
            conexion.commit()
        registrar_evento("INFO", "Base de datos inicializada correctamente.")
    except Exception as e:
        registrar_evento("ERROR", f"Error al inicializar la base de datos: {e}")
        