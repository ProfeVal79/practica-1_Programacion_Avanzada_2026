#Definir una funcion llamada calculo_liquido que reciba 3 numeros, el alto, el ancho y la
#profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene. 

def calculo_liquido(alto, ancho, profundidad):
    volumen = alto * ancho * profundidad
    liquido = volumen * 1000
    return liquido


alto_pileta = float(input("ingrese el alto de su pileta: "))
ancho_pileta = float(input("ingrese el ancho de su pileta: "))
prof_pileta = float(input("ingrese la profundidad de su pileta: "))
print("Su pileta tiene: ", calculo_liquido(alto_pileta, ancho_pileta, prof_pileta),"litros")    

#hago el calculo del volumen (alto * ancho * profundidad)
#luego lo convierto a liquido multiplicando por mil. para que el resultado me de en litros. 