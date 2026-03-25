#Definir una función denominada cuantos_dias, que reciba el numero de mes como parametro
#y retorne la cantidad de días que posee: Ejemplo: cuantos_dias(1) debería retornar 31.
#ayuda: Pensar en tener una lista de la siguiente manera: [["Enero", 31], ["Febrero", 28]...]
def cuantos_dias(numero_mes):
    lista_meses =[[],["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril",30], ["Mayo", 31], ["Junio", 30], ["Julio", 31], ["Agosto", 31], ["Septiembre", 30], ["octubre", 31], ["Noviembre", 30], ["Diciembre", 31]]
    if numero_mes < 1 or numero_mes > 12:
        return f"El mes indicado no existe"
    else:
     return lista_meses[numero_mes][1]

mes_elegido = int(input("ingrese el numero de mes: "))
cantidad_dias = cuantos_dias(mes_elegido)
print(f"el mes indicado tiene: {cantidad_dias} días")

#En la lista, primero agrego una lista vacia, para que tome los meses reales,
#ya que la primera estaría en la pocisión "0". 
#primero evalúa que el mes dado este en el rango indicado entre 1 y 12. 
#si el mes es menor a 1 o mayor a 12, nos devolvera un mensaje "el mes indicado no existe"