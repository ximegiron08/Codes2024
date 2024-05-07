import mymathlib

while True:
    print("Seleccione el cálculo que desea realizar:")
    print("1. Cálculo de velocidad")
    print("2. Cálculo de distancia")
    print("3. Cálculo de tiempo")
    print("4. Cálculo de volumen de un cubo")
    print("5. Cálculo de fuerza")
    print("6. Cálculo de trabajo")
    print("7. Cálculo de potencia")
    print("8. Cálculo de presión") 
    print("9. Cálculo de densidad")
    print("10. Cálculo de área de un rectángulo")
    print("11. salir del programa")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        distancia=float(input("Ingrese el tiempo en segundos: "))
        tiempo=float(input("ingrese la distancia en metros: "))
        print(f"la velocidad es de:", {mymathlib.velocidad(distancia,tiempo)}," m/s")
    elif opcion == '2':
        velocidad=float(input("Ingrese la velocidad en m/s: "))
        tiempo=float(input("ingrese el tiempo en segundos: "))
        print("la distancia es de:", {mymathlib.distancia(velocidad,tiempo)}," metros")
    elif opcion == '3':
         distancia=float(input("Ingrese la distancia en metros: "))
         velocidad=float(input("ingrese la velocidad en m/s: "))
         print(f"el tiempo es de:", {mymathlib.tiempo(distancia,velocidad)}," segundos")
    elif opcion == '4':
         lado=float(input("Ingrese el lado del cubo en metros: "))
         print(f"el volumen del cubo es de:", {mymathlib.vol_cubo(lado)}," metros cúbicos")
    elif opcion == '5':
        masa=float(input("Ingrese la masa en kilogramos: "))
        aceleracion=float(input("ingrese la aceleración en m/s^2: "))
        print(f"la fuerza es de:", {mymathlib.fuerza(masa, aceleracion)}," Newtons")
    elif opcion == '6':
        fuerza=float(input("Ingrese la fuerza en Newtons: "))
        desplazamiento=float(input("ingrese el desplazamiento en metros: "))
        print(f"el trabajo es de:", {mymathlib.trabajo(fuerza, desplazamiento)}," Joules")
    elif opcion == '7':
        trabajo=float(input("Ingrese el trabajo en Joules: "))
        tiempo=float(input("ingrese el tiempo en segundos: "))
        print(f"la potencia es de:", {mymathlib.potencia(trabajo, tiempo)}," Joule/s")
    elif opcion == '8':
        fuerza=float(input("Ingrese la fuerza en Newtons: "))
        superficie=float(input("ingrese la superficie m^2: "))
        print(f"la presión es de:", {mymathlib.presion(fuerza, superficie)}," Pascal")
    elif opcion == '9':
        masa=float(input("Ingrese la masa en kilogramos: "))
        velocidad=float(input("ingrese la velocidad en m/s: "))
        print(f"la densidad es de:", {mymathlib.densidad(masa, velocidad)}," kg/m³")
    elif opcion == '10':
        base=float(input("Ingrese la base del rectángulo en metros: "))
        altura=float(input("ingrese la altura del rectángulo en metros: "))
        print(f"El área del rectángulo es de:", {mymathlib.area_rectangulo(base, altura)}," metros")
    elif opcion == '11':
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")