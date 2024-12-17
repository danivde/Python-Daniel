import pandas as pd

# Paso 1: Crear dos Series de Pandas a partir de listas de datos

# Datos de temperatura semanal (Serie A)
temperaturas = [22, 24, 26, 28, 30, 32, 31]  # en grados Celsius
serie_A = pd.Series(temperaturas, name="Temperaturas")

# Datos de precipitación semanal (Serie B)
precipitacion = [5, 10, 15, 0, 2, 7, 3]  # en milímetros
serie_B = pd.Series(precipitacion, name="Precipitación")

# Mostrar las dos Series
print("Serie A - Temperaturas:")
print(serie_A)
print("\nSerie B - Precipitación:")
print(serie_B)

# Paso 2: Realizar operaciones de slicing en ambas Series

# Slicing: seleccionar los primeros 4 elementos de ambas Series
slicing_A = serie_A[:4]  # Primeros 4 elementos de la Serie A
slicing_B = serie_B[:4]  # Primeros 4 elementos de la Serie B

# Mostrar los resultados del slicing
print("\nSlicing de la Serie A (primeros 4 elementos):")
print(slicing_A)
print("\nSlicing de la Serie B (primeros 4 elementos):")
print(slicing_B)

# Paso 3: Combinar las Series resultantes del slicing en una nueva Serie

# Combinar las Series usando pd.concat
combinada = pd.concat([slicing_A, slicing_B], axis=1)

# Mostrar la Serie combinada
print("\nSerie combinada (Temperaturas y Precipitación):")
print(combinada)

# Paso 4: Realizar operaciones básicas en la Serie combinada

# Calcular el promedio de temperatura y precipitación
promedio_temperatura = combinada["Temperaturas"].mean()
promedio_precipitacion = combinada["Precipitación"].mean()

# Mostrar los promedios
print("\nPromedio de Temperatura en las primeras 4 semanas:", promedio_temperatura)
print("Promedio de Precipitación en las primeras 4 semanas:", promedio_precipitacion)

# Realizar una operación combinada: Temperatura + Precipitación
combinada["Total"] = combinada["Temperaturas"] + combinada["Precipitación"]

print("\nSerie combinada con la columna 'Total' (Temperatura + Precipitación):")
print(combinada)
