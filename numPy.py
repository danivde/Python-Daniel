import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset y seleccionar columnas relevantes
url = "path_to_IMDB-Movie-Data.csv"  # Cambia esto por la ruta local de tu archivo descargado.
data = pd.read_csv(url)
columns_to_select = ['Title', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']
data = data[columns_to_select]

# 2. Manejar valores faltantes en 'Revenue (Millions)'
data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean(), inplace=True)

# Convertir a array de Numpy
numpy_data = data.to_numpy()

# Análisis Estadístico
# 3. Calcular la calificación promedio de las películas
average_rating = np.mean(numpy_data[:, 3])
print(f"Calificación promedio de las películas: {average_rating:.2f}")

# 4. Encontrar la película con la duración más larga
max_runtime_index = np.argmax(numpy_data[:, 2])
longest_movie = numpy_data[max_runtime_index, 0]
print(f"Película con la duración más larga: {longest_movie}")

# 5. Determinar el ingreso promedio y la mediana
average_revenue = np.mean(numpy_data[:, 5])
median_revenue = np.median(numpy_data[:, 5])
print(f"Ingreso promedio: ${average_revenue:.2f}M")
print(f"Ingreso mediano: ${median_revenue:.2f}M")

# Manipulación de Datos
# 6. Crear subconjunto de películas de los últimos 10 años
current_year = pd.Timestamp.now().year
recent_movies = data[data['Year'] >= (current_year - 10)]
recent_votes_avg = recent_movies['Votes'].mean()
print(f"Promedio de votos para películas de los últimos 10 años: {recent_votes_avg:.0f}")

# Correlación
# 7. Evaluar correlación entre calificación y los ingresos
ratings
