def segundos_a_minutos():
    segundos=int(input("Ingrese la cantidad de segundos: "))
    minutos = segundos / 60
    print(f"{segundos} segundos equivalen a {minutos} minutos.")

def minutos_a_horas():
    minutos=int(input("Ingrese la cantidad de minutos: "))
    horas = minutos / 60
    print(f"{minutos} minutos equivalen a {horas} horas.")

def horas_a_segundos():
    horas=int(input("Ingrese la cantidad de horas: "))
    segundos = horas * 3600
    print(f"{horas} horas equivalen a {segundos} segundos.")


while True:
    print("Seleccione la conversión que desea realizar:")
    print("1. Segundos a minutos")
    print("2. Minutos a horas")
    print("3. Horas a segundos")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        segundos_a_minutos() 
    elif opcion == '2':
        minutos_a_horas() 
    elif opcion == '3':
        horas_a_segundos() 
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")