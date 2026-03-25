#Definir una función que calcule el área de un circulo, otra que calcule el área 
#rectángulo, otra que calcule el área de un cuadrado.
#Analice que parametros deberian recibir dichas funciones. 

def Area_Circulo(radio):
    pi = 3.1416
    area = pi * (radio**2)
    return area

print(Area_Circulo(4))

def Area_rectangulo(base, altura):
    area = base * altura
    return area

print(Area_rectangulo(2,4))

def Area_cuadrado(lado):
    area = lado**2
    return area

print(Area_cuadrado(4))

#En el circulo solo necesita el radio (1 parametro), 
#en el rectángulo base y altura (2 parametros),
#en el cuadrado solo el lado (1 parametro)

