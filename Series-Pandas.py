import pandas as pd
# Paso 1: Crear la Serie a partir de una lista de números
numeros = [10, 20, 30, 40, 50]
serie = pd.Series(numeros)

# Paso 2: Mostrar la Serie
print("Serie original:")
print(serie)

# Paso 3: Agregar un nuevo elemento a la Serie
serie[5] = 60  # Agregamos un número en la posición 5
print("\nSerie después de agregar un nuevo elemento (60):")
print(serie)

# Paso 4: Quitar un elemento de la Serie
serie = serie.drop(2)  # Esto elimina el elemento con índice 2
print("\nSerie después de eliminar el elemento con índice 2:")
print(serie)

# Paso 5: Realizar operaciones aritméticas básicas (suma, resta, multiplicación y división)
suma = serie + 10        # Sumar 10 a cada elemento
resta = serie - 5        # Restar 5 a cada elemento
multiplicacion = serie * 2  # Multiplicar cada elemento por 2
division = serie / 2      # Dividir cada elemento por 2

# Paso 6: Mostrar resultados
print("\nOperaciones aritméticas:")
print(f"Suma +10: \n{suma}")
print(f"Resta -5: \n{resta}")
print(f"Multiplicación por 2: \n{multiplicacion}")
print(f"División por 2: \n{division}")
