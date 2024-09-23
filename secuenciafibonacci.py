print("bienvenido al programa de cálculo de la secuencia de Fibonacci")
print("ingrese el número de términos que desea calcular")
n = int(input())
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci)
print("Gracias por usar el programa :)")