
# Lista de empleados
empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

for empleado in empleados:
    print(empleado[0], "tiene habilidades:", ", ".join(empleado[1]), "\n")

import copy

# Lista de empleados
empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

# Copia superficial y profunda
empleados_copy_superficial = empleados.copy()
empleados_copy_profunda = copy.deepcopy(empleados)

# Modificar las habilidades de Pedro en la lista original
empleados[0][1].append("JavaScript" , )
empleados [0] [1] . append("Office" , )

# Modificar Alejandro 
empleados [2][1]. append("Python" ,) #Prueba para elegir otro nombre

# Imprimir la lista original
print("Lista Original:")
for empleado in empleados:
    print(empleado[0] + "\n", "Habilidades:", ", ".join(empleado[1]), "\n") #Salto de linea

# Imprimir la copia superficial
print("Copia Superficial:")
for empleado in empleados_copy_superficial:
    print(empleado[0] + "\n", "Habilidades:", ", ".join(empleado[1]), "\n") #Salto de linea

# Imprimir la copia profunda
print("Copia Profunda:")
for empleado in empleados_copy_profunda:
    print(empleado[0] + "\n", "Habilidades:", ", ".join(empleado[1]), "\n") #Salto de linea

