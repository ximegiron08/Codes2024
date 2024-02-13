
for _ in range(10):
    numerodecarne=input("ingrese el número de carné del alumno")
    if len(numerodecarne)==8:
        nombreyapellido=input("ingrese el nombre y el apellido del alumno")      
        print("los alumnos y sus carnés son:" ,numerodecarne, nombreyapellido)
    else:
        print("carne invalido, alumno no ingresado")