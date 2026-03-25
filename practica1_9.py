#definir una función llamada calculo_nuevo_precio, que reciba dos números, uno con el precio
#anterior y otro con el numero de porcentaje a aumentar y devuelva el precio aumentado. 

def calculo_nuevo_precio(precio, porcentaje):
    nuevo_precio = precio + (precio * porcentaje /100)
    return nuevo_precio

precio_anterior = float(input("Ingrese el precio anterior: "))
porcentaje_aumentar = float(input("Ingrese el porcentaje a aumentar: "))
print("El nuevo precio es:$",calculo_nuevo_precio(precio_anterior, porcentaje_aumentar))

#primero se resuelve los parentesis, que es el precio multiplicado por el por el
# valor(porcentaje) pasado dividido en 100. y luego lo suma al precio anterior.
# Esto me devuelve el precio aumentado.  
