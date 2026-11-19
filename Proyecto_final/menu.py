from colores import titulo, mostrar_exito
from productos import(
    registrar_producto,
    listar_productos,
    buscar_producto,
    actualizar_producto,
    eliminar_producto
)
from reportes import reporte_stock_bajo

def mostrar_menu():
    
    while True:  
        titulo("Sistema de Gestion de Inventario")
        print("1. Registrar nuevo producto")
        print("2. Visualizar productos")
        print("3. Buscar productos")
        print("4. Actualizar producto por ID")
        print("5. Eliminar producto por ID")
        print("6. Reporte de stock bajo")
        print("7. salir")
        
        opcion = input("\nSeleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_stock_bajo()
        elif opcion == "7":
            mostrar_exito("¡Gracias por usar el sistema de inventario. Hasta luego! ")
            break
        else:
            print("[X] Opcion no válida. Por favor, ingrese un número entre 1 y 7.")
            input("\nPresione Enter para continuar...")
            