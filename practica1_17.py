#Definir una función que reciba como parametro una lista de numeros y retome la suma del primer
#elemento con el ultimo. 
#Zona de definicines:
def SumaPrimUlt(lista):
    return lista[0] + lista[-1]


#Retorna la suma entre el primer elemento posición [0] y el ultimo elemento posición [-1]

def promedioPrimUlt(lista):
    suma = lista[0] + lista[-1]
    return suma/2 


#retorna el promedio entre el primer elemento y el ultimo. 

#Zona programa principal: Solicitar al usuario 3 números, armar la lista e invocar las funciones:

n1 = int(input("Ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
n3 = int(input("ingrese el ultimo numero: "))
mi_lista = []
mi_lista.append(n1)
mi_lista.append(n2)
mi_lista.append(n3)

print("La suma del primer y ultimo numero es: ", SumaPrimUlt(mi_lista))
print("El promedio del primer y ultimo numero es: ", promedioPrimUlt(mi_lista))

