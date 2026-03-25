#Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto dado
#su precio de venta sin IVA. 

def precio_con_iva(precio):
    con_iva = precio + (precio/100*21)
    return con_iva

print(precio_con_iva(10000))