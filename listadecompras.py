lista=[]
for _ in range(50):
    item=input(("ingrese un item:"))
    if item=="fin":
        print("se cierra la lista de compras")
        break
    else:
        lista.append(item)
print("la lista es",lista)
while True:
    eliminar=input("¿quiere eliminar un item?")
    if eliminar=="si":
        item=input("¿que item quiere borrar?:")
        lista.remove(item)
    elif eliminar=="no":
        print("los items son:")
        print("la nueva lista es:",lista)
    elif eliminar=="fin":
        print("se cierra la lista de compras nuevamente")
        break