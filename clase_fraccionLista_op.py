class FraccionLista:
    def __init__(self, fraccion):
        self.fraccion = fraccion

    def CargarFraccion(self):
     numerador = int(input("Ingrese el numerador: "))
     denominador = int(input("Ingrese el denominador: "))
     self.fraccion = []
     self.fraccion.append(numerador)
     self.fraccion.append(denominador)
     print(f"{numerador}/{denominador}")
     return [numerador, denominador]

    def numeradorFraccion(self):
        return self.fraccion[0]

    def denominadorFraccion(self):
        return self.fraccion[1]

    def SumaFracciones(self, otra):
        num1 = self.numeradorFraccion()
        den1 = self.denominadorFraccion()
        num2 = otra.numeradorFraccion()
        den2 = otra.denominadorFraccion()
        denominador = den1 * den2
        numerador = denominador / den1 * num1 + denominador / den2 * num2
        return [numerador, denominador]

    def RestaFracciones(self, otra):
        num1 = self.numeradorFraccion()
        den1 = self.denominadorFraccion()
        num2 = otra.numeradorFraccion()
        den2 = otra.denominadorFraccion()
        denominador = den1 * den2
        numerador = denominador / den1 * num1 - denominador / den2 * num2
        return [numerador, denominador]
    
    def DivisionFacciones(self, otra):
        num1 = self.numeradorFraccion()
        den1 = self.denominadorFraccion()
        num2 = otra.numeradorFraccion()
        den2 = otra.denominadorFraccion()
        numerador = num1 * den2
        denominador = den1 * num2
        return [numerador, denominador]

    def MultiplicacionFracciones(self, otra):
        num1 = self.numeradorFraccion()
        den1 = self.denominadorFraccion()
        num2 = otra.numeradorFraccion()
        den2 = otra.denominadorFraccion()
        numerador = num1 * num2
        denominador = den1 * den2
        return [numerador, denominador]

#instancias
print("Bienvenidos/as a cuentas con fracciones")
a = FraccionLista([0, 1])
b = FraccionLista([0, 1])
print("Ingrese la primer fracción: ", a.CargarFraccion())
print("ingrese la segunda fracción: ", b.CargarFraccion())
print("El denominador de la primer fracción es: ", a.denominadorFraccion())
print("El numerador de la segunda fracción es: ", b.numeradorFraccion())
print("La suma de dichas fracciones es: ", a.SumaFracciones(b))
print("La resta de dichas fracciones es: ", a.RestaFracciones(b))
print("La división de dichas fracciones es: ", a.DivisionFacciones(b))
print("La multiplicación de dichas fracciones es: ", a.MultiplicacionFracciones(b))


    

