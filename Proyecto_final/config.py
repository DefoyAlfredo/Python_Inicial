from pathlib import Path
# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent
# Ruta de la base de datos y del registro de log
DB_PATH = BASE_DIR /"inventario.db"
LOG_PATH = BASE_DIR / "app.log"
