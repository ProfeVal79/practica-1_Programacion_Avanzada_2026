from cargarFraccion import CargarFraccion
from denominadorFraccion import DenominadorFraccion
from numeradorFraccion import numeradorFraccion
from SumaFracciones import SumaFracciones
from RestaFracciones import RestaFracciones
from DivisionFracciones import DivisionFacciones
from MultiplicacionFracciones import MultiplicacionFracciones
print("Bienvenidos/as a cuentas con fraciones")
a = CargarFraccion()
b = CargarFraccion()
print("El denominador de la primer fraccion es: ", DenominadorFraccion(a))
print("El numerador de la segunda fraccion es: ", numeradorFraccion(b))
print("La suma de dichas fracciones es: ", SumaFracciones(a,b))
print("La resta de dichas fracciones es: ", RestaFracciones(a,b))
print("La multiplicación de dichas fracciones es: ", MultiplicacionFracciones(a,b))
print("La división de dichas fracciones es: ", DivisionFacciones(a,b))

