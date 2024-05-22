#Realizado por: Xime Girón
#Examen final segunda unidad sistemas e instalación
#Raúl Bojórquez
#22/05/2024

print("bienvenido al programa para el cálculo de la tarifa de un viaje en Uber Guatemala")
distancia_km = float(input("Ingrese la distancia recorrida en kilómetros: "))
tiempo_min = int(input("Ingrese el tiempo de viaje en minutos: "))
hora_viaje = int(input("Ingrese la hora del día (hora de inicio del viaje): "))

tarifa_base = 5.00
tarifa_por_km = 2.50
tarifa_por_min = 0.50

tarifa_total = tarifa_base

tarifa_total += distancia_km * tarifa_por_km

tarifa_total += tiempo_min * tarifa_por_min

if (hora_viaje >= 7 and hora_viaje < 9) or (hora_viaje >= 17 and hora_viaje < 19):
    recargo = tarifa_total * 0.20
    tarifa_total += recargo

print("El costo total del viaje es: Q{:.2f}".format(tarifa_total))