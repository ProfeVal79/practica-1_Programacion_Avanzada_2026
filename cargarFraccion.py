def CargarFraccion():
 numerador = int(input("Ingrese el numerador: "))
 denominador = int(input("Ingrese el denominador: "))
 fraccion = []
 fraccion.append(numerador)
 fraccion.append(denominador)
 print(f"{numerador}/{denominador}")
 return [numerador, denominador]
