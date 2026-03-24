class Conversion:
    def __init__(self, pesos):
        self.pesos = pesos

    def convertir_a_dolar(self):
        dolar = self.pesos / valor_dolar
        return dolar

    def convertir_a_euro(self):
        euro = self.pesos / valor_euro
        return euro
    def convertir_a_real(self):
        real = self.pesos / valor_real
        return real

monto_pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
valor_dolar = 1425
valor_euro = 1545
valor_real = 285
mi_conversion = Conversion(monto_pesos)
resultado_dolar = mi_conversion.convertir_a_dolar()
resultado_euro = mi_conversion.convertir_a_euro()
resultado_real = mi_conversion.convertir_a_real()
print("Usted tiene: ", {resultado_dolar}, "USD")
print("Usted tiene: ", {resultado_euro}, "Euros")
print("Usted tiene: ", {resultado_real}, "Reales")

