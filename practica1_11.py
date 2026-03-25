#Definir una función llamada armo_cartel que reciba una cadena de caracteres para el nombre
# del producto y dos numeros (el precio y el precio rebajado) e imprima un cartel así:
# Atención!!! Gran rebaja para el producto (parametro)!!!
#Antes: (precio anterior)
#Ahora: (precio rebajado)

def armo_cartel(producto, precio_anterior, precio_rebajado):
    return f"Atención!!! Gran rebaja para el producto: {producto}!!!\n Antes:${precio_anterior}\n Ahora ${precio_rebajado}"

print(armo_cartel("Tomate", 1500, 800))

#el uso "\n" es para el salto de linea y el cartel quede como el sugerido.