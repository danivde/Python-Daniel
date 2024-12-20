# peliculas proyecto parte 2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify, render_template

# Cargar el conjunto de datos
data_url = "https://www.kaggleusercontent.com/datasets/PromptCloudHQ/imdb-data"  # Asegúrate de descargar y colocar el archivo localmente
file_path = "imdb.csv"  # Cambia esto si el archivo tiene otro nombre
data = pd.read_csv(file_path)

# Preprocesar los datos
# Nos aseguramos de que los datos no tengan valores nulos en las columnas importantes
data = data.dropna(subset=['Title', 'Genre', 'Description'])

# Crear una columna combinada para representar las características clave
data['Combined'] = data['Genre'] + " " + data['Description']

# Convertir texto a una representación numérica
vectorizer = TfidfVectorizer(stop_words='english')
features = vectorizer.fit_transform(data['Combined'])

# Definir la función de recomendación
def recommend_movies(movie_title, num_recommendations=5):
    # Verificar si la película está en el conjunto de datos
    if movie_title not in data['Title'].values:
        return []

    # Obtener el índice de la película dada
    movie_idx = data[data['Title'] == movie_title].index[0]

    # Calcular la similitud de coseno entre la película dada y todas las demás
    cosine_sim = cosine_similarity(features[movie_idx], features)

    # Obtener los índices de las películas más similares
    similar_indices = cosine_sim[0].argsort()[-num_recommendations-1:-1][::-1]

    # Recuperar los títulos de las películas recomendadas
    recommendations = data.iloc[similar_indices]['Title'].tolist()
    return recommendations

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie')
    recommendations = recommend_movies(movie_title)
    if not recommendations:
        return jsonify({"error": f"La película '{movie_title}' no está en el conjunto de datos."})
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
