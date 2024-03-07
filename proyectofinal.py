
print("Bienvenid@ al registro de especies del ecosistema.")
print("Ingrese el nombre de las especies avistadas, cuando termine de ingresar todas las especies, escriba 'fin'.")

especies = {}
while True:
        especie = input("Ingrese el nombre de la especie avistada o escriba 'fin' para cerrar la lista: ")
        if especie.lower() == 'fin':
            break
        especies[especie] = especies.get(especie, 0) + 1

print("Informe de las especies avistadas:")
for especie, cantidad in especies.items():
        print(f"{especie}: {cantidad}")
        especie_mas_comun = max(especies, key=especies.get)
cantidad_mas_comun = especies[especie_mas_comun]
print(f"La especie más común en el ecosistema es '{especie_mas_comun}' con {cantidad_mas_comun} avistamientos.")
print("Gracias por usar el programa de registro de especies del ecosistema, espero haya sido de su utilidad.")