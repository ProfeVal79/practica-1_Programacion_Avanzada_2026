def RestaFracciones(x,y):
  denominador = x[1] * y[1]
  numerador = denominador / x[1] * x[0] - denominador / y[1] * y[0]
  return [numerador, denominador]