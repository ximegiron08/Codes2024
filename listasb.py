inventario = []
def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f"Producto '{nombre}' agregado")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def actualizar_cantidad():
    nombre = input("Nombre del producto: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            nueva_cantidad = int(input("Nueva cantidad: "))
            producto["cantidad"] = nueva_cantidad
            print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def consultar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

def mostrar_menu():
    print("Menú de Inventario")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar el producto")
    print("4. Consultar inventario")
    print("5. Salir")

def gestionar_inventario():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            actualizar_cantidad()
        elif opcion == '4':
            consultar_inventario()
        elif opcion == '5':
            print("Has salido del programa.")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

mostrar_menu()
gestionar_inventario()
consultar_inventario()
actualizar_cantidad()
eliminar_producto()
agregar_producto()