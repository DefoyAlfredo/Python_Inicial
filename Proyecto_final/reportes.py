from base_datos import obtener_conexion
from colores import mostrar_info, mostrar_error, titulo
from validaciones import leer_entero

def reporte_stock_bajo():
    titulo("Reporte de Productos con Stock Bajo")
    limite = leer_entero("Ingrese el limite maximo de cantidad para el reporte:")
    
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM WHERE cantidad <= ?", (limite,))
            productos = cursor.fetchall()
            
            if not productos:
                mostrar_info(f"No hay productos con una cantidad igual o inferior a {limite}. ")
                return 
            
            print(f"\n--- PRODUCTOS CON STOCK <= {limite} ---")
            for p in productos:
                print(f"ID: {p['id']} | Nombre: {p['nombre']} | Stock: {p['cantidad']} | Precio: {p['precio']:.2f} | cat: {p['categoria']}")
    except Exception as e:
        mostrar_error(f"Error al generar el reporte: {e}")
        