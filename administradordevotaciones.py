dpi=input("ingrese su dpi")
cantidad=len(dpi)
if cantidad ==13:
    print("los partidos de presidencia a votar son: 1) partido rojo, 2) partido azul")
    presidente=input("ingrese el nombre del partido por el cual quiere votar:")
    if presidente=="partido rojo":
        print("votó rojo")
    elif presidente=="partido azul":
            print("votó azul")
    else:
        print("voto invalido")

    print("los partidos de alcalde a votar son: 1) partido amarillo, 2) partido morado, 3) partido verde, 4) partido naranja")
    alcalde=input("ingrese el nombre del partido por el cual quiere votar:")
    if alcalde=="partido amarillo":
        print("votó amarillo")
    elif alcalde=="partido morado":
        print("votó morado")
    elif alcalde=="partido verde":
        print("votó verde")
    elif alcalde=="partido naranja":
        print("votó naranja")
    else:
        print("voto invalido")
        alcalde="invalido"
        presidente="invalido"


    print("tu persona con dpi",dpi, "para presidente votarás por", presidente," y para alcalde votarás por", alcalde)
    respuesta=input("quiere guardar sus votos? si o no") 

    
    if respuesta=="si":
        print("se guardó su voto")
    if respuesta=="no":
        print("votos no guardados")

else:
    print("dpi invalido")
    print("intente de nuevo")
