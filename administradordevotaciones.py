dpi=input("ingrese su dpi")
cantidad=len(dpi)
if cantidad ==13:
    print("los partidos de presidencia a votar son: 1) partido rojo, 2) partido azul")
    presidente=input("ingrese el nombre del partido por el cual quiere votar:")
    print("los partidos de alcalde a votar son: 1) partido amarillo, 2) partido morado, 3) partido verde, 4) partido naranja")
    alcalde=input("ingrese el nombre del partido por el cual quiere votar:")
    print("tu persona con dpi",dpi, "para presidente votarás por", presidente," y para alcalde votarás por", alcalde)
else:
    print("dpi invalido")