#Definir una función llamada calculo_dosis que reciba tres numeros. Uno para la cantidad de
#dias que debe suministrar el remedio, el segundo dato para la cantidad de veces que debe tomarlo
#y el ultimo dato para la cantidad de comprimido que trae el envase.
#La función debe devolver "verdadero" si el envase alcanza para el tratamiento y "falso" si no alcanza.

def calculo_dosis(dias_trat, dosis_dia, dosis_envase):
    dosis_total = dosis_dia * dias_trat
    if dosis_total <= dosis_envase:
        return True
    else:
        return False

print(calculo_dosis(7, 4, 30))