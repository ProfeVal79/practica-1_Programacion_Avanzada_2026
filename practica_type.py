def dice(self):
    return "guauuu"
Animal = type("Perro",() ,{"nombre":"Firulais"})
Perro = type("", (Animal, ), dict(raza = "Dogo", cantidad_patas = 4, dice = dice))

p = Perro()
print(p.nombre)
print(p.cantidad_patas)
print(p.dice())
print(f"hola soy {p.nombre} mi raza es {p.raza}, tengo {p.cantidad_patas} patas y digo {p.dice()}")

Persona = type("", (),{"nombre": "Pedro", "edad": 45, "sexo": "hombre"})
Empleado = type("", (Persona, ), dict(puesto = "administración", antiguedad = 40, salario = "$1200000"))

h = Persona()
print(f"hola soy {h.nombre} tengo {h.edad} y soy {h.sexo}")

e = Empleado()
print(f"mi nombre es {e.nombre}, soy empleado en {e.puesto} mi antigüedad es {e.antiguedad} años y mi salario es {e.salario}")