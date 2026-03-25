#Definir una función llamada calculo_rebaja que reciba dos numero, 
#uno con el precio anterior, otro con el precio rebajado y devuelva
#un número que represente el porcentaje rebajado. 

def calculo_rebaja(precio_original, precio_rebajado):
    rebaja = precio_original - precio_rebajado
    porcentaje = rebaja * 100 / precio_original
    return round(porcentaje, 2)

precio = float(input("Ingrese el valor real: "))
precio_final = float(input("Ingrese el valor final: "))
print("Usted obtuvo un: ", calculo_rebaja(precio, precio_final), "% de descuento")

#primero le resta al precio anterior el precio rebajado (calculo rebaja)
#luego a esa rebaja (la diferencia) la multiplica por 100 
#y la divide por el precio anterior (esto me va a devolver el porcentaje de rebaja)
#el round en el return es para que me redondee los decimales a "2" el valor que le paso. 