"""
is Keyword 
Valida if dos objetos son el mismo objeto

Se utiliza para  validar si dos variables estan referenciadas al mismo objeto
Return:
True -> si son iguales
False -> no son el mismo objeto
"""

# Ejemplo

x = ["Nombre", "Apellido", "Valor"]

y = x

print (x is y)

a = ["Nombre", "Apellido", "Valor"]

b = ["Nombre", "Apellido", "Persona"]

print(a is b)


