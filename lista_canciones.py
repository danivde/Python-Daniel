#lista_canciones
# Gestion Lista de Canciones
# Escenario: Tenemos dos listas de canciones con sus duraciones en minutos

import random

# Listas iniciales de canciones y duraciones
canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01] # Duraciones en minutos

# Nueva lista de canciones y duraciones adicionales
canciones_nuevas = ["Thunderstruck", "Back In Black", "Thriller" ,]
duraciones_nuevas = [4.52, 4.14, 5.56]

# Combinar listas
canciones.extend(canciones_nuevas)
duraciones.extend(duraciones_nuevas)

#Combinar las dos listas en un diccionario
canciones_dict = dict(zip(canciones, duraciones))
print("\nDiccionario de canciones:")
print(canciones_dict)

#Seleccionar las 3 canciones más largas
canciones_ordenadas = sorted(canciones_dict.items(), key=lambda x: x[1], reverse=True)
tres_mas_largas = dict(canciones_ordenadas[:3])
print("\nTres canciones más largas:")
print(tres_mas_largas)

#Selección aleatoria de canciones
numero_seleccion = 3  # Número de canciones a seleccionar
seleccion_aleatoria = dict(random.sample(canciones_dict.items(), numero_seleccion))
print("\nSelección aleatoria de canciones:")
print(seleccion_aleatoria)
