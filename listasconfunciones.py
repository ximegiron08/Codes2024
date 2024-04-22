lista=[]
def emprezarlista():
    for _ in range(50):
        item=input("ingrese un item:")
        if item=="fin":
            print("se cierra la lista de compras")
            break
        else:
            lista.append(item)
emprezarlista()

def agregar():
    item=input("ingrese un item:")
    lista.append(item)

def remover():
    item=input("¿Qué item quiere eliminar?:")
    lista.remove(item)

while True:
    print("Seleccione la opción que desea realizar:")
    print("1. Agregar un  item")
    print("2. Remover un item")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        agregar() 
    elif opcion == '2':
        remover() 
    elif opcion == '3':
        print("Se cierra la lista")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
print(lista)