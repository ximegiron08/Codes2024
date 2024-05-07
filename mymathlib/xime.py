def velocidad(distancia, tiempo):
     velocidad = distancia/tiempo
     return velocidad


def distancia(velocidad, tiempo):
     distancia = velocidad*tiempo
     return distancia


def tiempo(distancia, velocidad):
     tiempo = distancia/velocidad
     return tiempo
print(tiempo)

def vol_cubo(lado):
     volumen = lado*lado*lado
     return volumen
print(vol_cubo)

def fuerza(masa, aceleracion):
     return masa*aceleracion
print(fuerza)

def trabajo(fuerza, desplazamiento):
     return fuerza*desplazamiento
print(trabajo)

def potencia(trabajo, tiempo):
     return trabajo/tiempo
print(potencia)

def presion(fuerza, superficie):
     return fuerza/superficie
print(presion)

def densidad(masa, velocidad):
     return masa/velocidad
print(densidad)

def area_rectangulo(base, altura):
     return base*altura
print(area_rectangulo)