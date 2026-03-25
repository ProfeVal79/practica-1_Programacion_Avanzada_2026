#Dado el siguiente código, indique cuales son los parametros reales y los formales.
#parametros formales: (x,y)
def SumaAlcuadrado(x,y):
    rta = x**2+2*x*y+y**2
    return rta


#si no aclaramos que es int/float nos da un error (el input directamente toma una cadena)
print("Bienvenidos a la suma al cuadrado")
a = int(input("ingrese un valor de a: "))
b = int(input("Ingrese un valor de b: "))
#parametros reales(a,b)
print(SumaAlcuadrado(a,b))
