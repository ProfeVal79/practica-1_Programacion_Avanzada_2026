#Definir una función que reciba un número como parametro y mostrar la table de multiplicar
#de dicho numero. 

def tabla_de_multiplicar(numero):
  for i in range(1, 11):  
    resultado = numero * i
    print( f"{numero} x {i} = {resultado}")

num = int(input("Ingrese un número: "))
tabla_de_multiplicar(num)

#En el bucle for (inicio, fin) el bucle se detiene al llegar al ultimo numero, 
#para que no se detenga en el 9 si yo le pasara (1, 10), y incluya al 10, le paso (1, 11). 
#lleva un print en lugar de un return, porque sino se detendria al
#llegar al primer resultado.



