
import statistics

# Ejemplo de lista de personas
personas = [
    {"nombre": "Juan", "ciudad": "Madrid", "salario": 1500},
    {"nombre": "Ana", "ciudad": "Barcelona", "salario": 2200},
    {"nombre": "Pedro", "ciudad": "Valencia", "salario": 1800},
    {"nombre": "María", "ciudad": "Sevilla", "salario": 2500},
    {"nombre": "Luis", "ciudad": "Bilbao", "salario": 1700},
    {"nombre": "Carmen", "ciudad": "Zaragoza", "salario": 2300},
    {"nombre": "Elena", "ciudad": "Málaga", "salario": 1900},
    {"nombre": "Raúl", "ciudad": "Granada", "salario": 2100},
    {"nombre": "Javier", "ciudad": "Murcia", "salario": 2000},
    {"nombre": "Sofia", "ciudad": "Córdoba", "salario": 2200}

]

# 1. Función para obtener salario de una persona
def get_salary(persona):
    return persona["salario"]

# 2. Función para listar personas de forma legible
def list_personas_legible(personas):
    for persona in personas:
        print(f"Nombre: {persona['nombre']}, Ciudad: {persona['ciudad']}, Salario: {persona['salario']}")

# 3. Mostrar primeras 5 personas
print("Primeras 5 personas:")
list_personas_legible(personas[:5])
print()

# 4. Calcular y mostrar el salario medio
salarios = [get_salary(persona) for persona in personas]
salario_medio = round(statistics.mean(salarios))  # Usamos statistics.mean para el promedio
print(f"Salario medio: {salario_medio}")

# 5. Calcular y mostrar la mediana del salario
mediana_salario = statistics.median(salarios)  # Usamos statistics.median para la mediana
print(f"Mediana del salario: {int(mediana_salario)}")  # Convertimos a entero

# 6. Calcular y mostrar la desviación estándar del salario
desviacion_estandar = round(statistics.stdev(salarios), 2)  # Usamos statistics.stdev para la desviación estándar
print(f"Desviación estándar del salario: {desviacion_estandar}")

# 7. Combinar ciudades y salarios en tuplas
ciudades = [persona["ciudad"] for persona in personas]
ciudades_salarios = list(zip(ciudades, salarios))

# Imprimir la quinta ciudad y su salario correspondiente
quinta_ciudad, quinto_salario = ciudades_salarios[4]
print(f"La quinta ciudad es {quinta_ciudad} con un salario de {quinto_salario}")

