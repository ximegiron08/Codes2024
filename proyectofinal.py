print("Bienvenid@ al programa de registro de especies.")
print("Este programa permite registrar las especies avistadas y realiza un informe de la distribucion de las especies avistadas en el ecosistema.")
avistamientos = {}
print("ingrese el nombre de la especie avistada en el ecosistema y escriba fin al terminar la lista")
while True:
    especie = input("nombre de la especie avistada: ")
    if especie.lower() == 'fin':
        break
    if especie in avistamientos:
        avistamientos[especie] += 1
    else:
        avistamientos[especie] = 1
print("el informe de la distribución de las especies avistadas es:")
for especie, cantidad in avistamientos.items():
    print(f"{especie}: {cantidad} avistamientos")
especie_mas_comun = max(avistamientos, key=avistamientos.get)
cantidad_de_avistamientos = avistamientos[especie_mas_comun]
print("la especie más común en el ecosistema es:", especie_mas_comun)
print("cantidad de avistamientos totales de la especie mas comun:", cantidad_de_avistamientos)
print("¡gracias por usar el pograma de registro de avistamientos de especies en un ecosistema!")
