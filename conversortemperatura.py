print("Bienvenido al conversor de grados Celsius y Farenheit, este es el menú de opciones:")
print("1. Conversión de grados Celsius a Farenheit")
print("2. Conversión de grados Farenheit a Celsius")
print("3. Salir")
opc = input("Ingrese la opción que desee: ")
if opc == "1":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {farenheit} grados Farenheit")
    
if  opc == "2":
    farenheit = float(input("Ingrese la temperatura en grados Farenheit: "))
    celsius = (farenheit - 32) * 5/9
    print(f"{farenheit} grados Farenheit son {celsius} grados Celsius")

if  opc == "3":
    print("¡Hasta luego! Gracias por usar nuestro conversor")