#Definir una función llamada calculo_transporte que reciba 4 números:
#la cantidad de alumnos de 1era, 2da y 3ra salita de un jardin de infantes,
#y la cantidad de asientos del transporte. La función debe retornar cuantos 
#micros escolares necesito contratar para la excursión. 
#Sabiendo que cada salita es acompañada por 3 adultos. 

def calculo_transporte(sala1, sala2, sala3, cant_asientos):
    sala1 = sala1 + 3
    sala2 = sala2 + 3
    sala3 = sala3 + 3
    cantidad_personas = sala1 + sala2 + sala3
    cantidad_micros = cantidad_personas //cant_asientos
    if cantidad_personas % cant_asientos > 0:
     cantidad_micros += 1
    return cantidad_micros

s1 = int(input("Ingrese la cantidad de alumnos para sala 1: "))
s2 = int(input("ingrese la cantidad de alumnos para sala 2: "))
s3 = int(input("ingrese la cantidad de alumnos para sala 3: "))

print("usted necesita: ", calculo_transporte(s1, s2, s3, 60))

# logica: a cada sala le sumo 3 adultos primero (para que las guarde cantidad + 3)
# cantidad_personas sumo las 3 salas
#cantidad de micros, cantidad_personas // cant_asientos
#// esto me va a dar cuantas personas entran en un micro
#if cantidad_personas % cantidad de asientos > 0: esto me va a decir cuantas personas sobran
#si hay mas personas que asientos, suma 1 micro. 