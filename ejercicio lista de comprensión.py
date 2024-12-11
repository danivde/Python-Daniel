# Lista de temperaturas experimentales (en grados Celsius)
temperaturas = [-300, -250, -200, -180, -150, -196, -100, 0, 25, 50, 100]

# Lista vacía para almacenar las temperaturas gaseosas
temperaturas_gaseosas = []

# Iteramos sobre la lista de temperaturas
for temp in temperaturas:
    if temp >= -196:
        temperaturas_gaseosas.append(temp)

# Imprimimos el resultado
print(temperaturas_gaseosas)

