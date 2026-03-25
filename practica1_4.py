#Definir una función denominada imprimir_fecha, que reciba tres cadenas de caracteres como parametros formales,
#que representan un día, un mes, un año e imprima la fecha de la siguiente manera:
#"21 de septiembre de 2025"

def imprimir_fecha(dia, mes, año):
    return f"{dia} de {mes} de {año}"

dia = input("escriba la fecha (día): ")
mes = input("Escriba el mes (ej. octube): ")
año = input("Escriba el año: ")
print(imprimir_fecha(dia, mes, año))

