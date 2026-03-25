#Definir una función denominada retorno_mensaje, que retorne el siguiente mensaje:
#"Estudiando en la UNAB"
#a) Como hago para mostrar ese mensaje en pantalla.
def retorno_mensaje():
    return "Estudiando en la UNAB"
print(retorno_mensaje())
#rta: llamando la función con un print.

#b)¿Que diferencia encuentra con el ejercicio anterior?
#rta: En el ejercicio anterior en el cuerpo de la función se define el print con el mensaje dentro.
#al llamar a la función solo imprime, porque esa es la instrucción. 
#En este ejercicia retorna (lo guarda en la memoria), pero no lo imprime. 

#c) Si tuvieras que imprimir mensajes como "Estudiando Matematica I en la UNAB"
#  y "Estudiando Python en la UNAB" utilizando la misma función. ¿Como lo modificarias?
def retorno_otro_mensaje(mensaje):
    return mensaje

print(retorno_otro_mensaje("Estudiando Matematica I en la UNAB"))
print(retorno_otro_mensaje("Estudiando Python en la UNAB"))