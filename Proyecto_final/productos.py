from base_datos import obtener_conexion
from colores import mostrar_exito, mostrar_error, mostrar_info, titulo
from registro_log import registrar_evento
from validaciones import leer_entero, leer_real, leer_texto

def registrar_producto():
    titulo("Registrar Nuevo Producto")
    nombre = leer_texto("Nombre del producto: ")
    descripcion = input("Descripción (opcional): ").strip()
    cantidad = leer_entero("Cantidad disponible: ")
    precio = leer_real("Precio del producto: ")
    categoria = input("Categoría (opcional): ").strip()

    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, descripcion, cantidad, precio, categoria))
            conexion.commit()
        mostrar_exito("¡Producto registrado con éxito!")
        registrar_evento("INFO", f"Producto registrado: {nombre}")
    except Exception as e:
        mostrar_error(f"Error al registrar el producto: {e}")
        registrar_evento("ERROR", f"Error al registrar producto: {e}")

def listar_productos():
    titulo("Lista de Productos Registrados")
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()

            if not productos:
                mostrar_info("No hay productos registrados en el inventario.")
                return

            for p in productos:
                print(f"ID: {p['id']} | Nombre: {p['nombre']} | Desc: {p['descripcion'] or 'N/A'} | "
                      f"Cant: {p['cantidad']} | Precio: ${p['precio']:.2f} | Cat: {p['categoria'] or 'N/A'}")
    except Exception as e:
        mostrar_error(f"Error al listar productos: {e}")

def buscar_producto():
    titulo("Búsqueda de Productos")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    opcion = input("Seleccione una opción de búsqueda: ").strip()

    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        if opcion == "1":
            id_prod = leer_entero("Ingrese el ID del producto: ")
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
            resultados = cursor.fetchall()
        elif opcion == "2":
            nombre = leer_texto("Ingrese el nombre o parte del nombre: ")
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
            resultados = cursor.fetchall()
        elif opcion == "3":
            categoria = leer_texto("Ingrese la categoría: ")
            cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{categoria}%",))
            resultados = cursor.fetchall()
        else:
            mostrar_error("Opción inválida.")
            return

        if not resultados:
            mostrar_info("No se encontraron productos con los criterios especificados.")
            return

        for p in resultados:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Cant: {p['cantidad']} | Precio: ${p['precio']:.2f} | Cat: {p['categoria']}")

def actualizar_producto():
    titulo("Actualizar Producto")
    id_prod = leer_entero("Ingrese el ID del producto a actualizar: ")

    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
        producto = cursor.fetchone()

        if not producto:
            mostrar_error("No existe un producto con ese ID.")
            return

        print(f"Actualizando a: {producto['nombre']}")
        nuevo_nombre = input(f"Nuevo nombre [{producto['nombre']}]: ").strip() or producto['nombre']
        nueva_desc = input(f"Nueva descripción [{producto['descripcion']}]: ").strip() or producto['descripcion']
        nueva_cant_str = input(f"Nueva cantidad [{producto['cantidad']}]: ").strip()
        nueva_cant = int(nueva_cant_str) if nueva_cant_str else producto['cantidad']
        nuevo_precio_str = input(f"Nuevo precio [{producto['precio']}]: ").strip()
        nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else producto['precio']
        nueva_cat = input(f"Nueva categoría [{producto['categoria']}]: ").strip() or producto['categoria']

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_cat, id_prod))
        conexion.commit()
        mostrar_exito("¡Producto actualizado correctamente!")
        registrar_evento("INFO", f"Producto ID {id_prod} actualizado.")

def eliminar_producto():
    titulo("Eliminar Producto")
    id_prod = leer_entero("Ingrese el ID del producto que desea eliminar: ")

    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
        if not cursor.fetchone():
            mostrar_error("No se encontró ningún producto con ese ID.")
            return

        confirmacion = input(f"¿Está seguro de eliminar el producto ID {id_prod}? (s/n): ").lower()
        if confirmacion == 's':
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
            conexion.commit()
            mostrar_exito("Producto eliminado correctamente.")
            registrar_evento("INFO", f"Producto ID {id_prod} eliminado.")
        else:
            mostrar_info("Operación cancelada.")