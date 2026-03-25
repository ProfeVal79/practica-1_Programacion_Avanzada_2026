#Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, 
#el monto gastado en bebidas, el monto gastado en comida, el alquiler del lugar y retorne
#cuanto le toca pagar a cada uno. 

def a_pagar(cant_pers, gasto_bebid, gasto_comida, alquiler):
    gastos_totales = gasto_bebid + gasto_comida + alquiler
    cantidad_a_pagar = gastos_totales / cant_pers
    return round(cantidad_a_pagar, 2)

cantidad_personas = int(input("ingrese la cantidad de personas: "))
gasto_bebidas = float(input("ingrese el gasto total en bebidad: "))
gasto_comidad = float(input("ingrese el gasto total en comida: "))
valor_alquiler = float(input("Ingrese el valor del alquiler: "))
print("el total a abonar por persona es:$ ",a_pagar(cantidad_personas, gasto_bebidas, gasto_comidad, valor_alquiler))