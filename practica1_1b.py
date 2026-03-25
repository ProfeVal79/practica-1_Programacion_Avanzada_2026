#Mencione los errores en los siguientes códigos:
#A)código:
#def Suma(par1, par2):
    #print(par1 + par2)


#Suma() #faltan los parametros reales.
#B)código:
#def Suma(par1, par2):
 #   print(par1 + par2)
#print(Suma(10,12))

# como la función solo tiene una instrucción de impresión y no un return,
# la función devuelve automaticamente el objeto None.
#en la invocación se llama a la función para que imprima con parametros reales.
#entonces primero imprime el resultado (invocación) e inmediatamente despues imprime None.

#C)código:
#def Suma(par1):
 #   return (par1 + 2)
#Suma(10, 12)   
#primer error, pasa un solo parametro formal y 2 parametros reales,
#segundo error, no tiene un print, osea solo lo guarda al resultado en la memoria,
#pero no muestra resultado. 
#La solución es pasar un solo parametro real y le sumaria dos a ese parametro,
#pero para que muestre el resultado hay que agregarle un print.
#Ejemplo: >>>print(Suma(10)) --> esto me devolvera 12

