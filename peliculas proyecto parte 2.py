import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify, render_template

# Cargar el conjunto de datos
data_url = "https://www.kaggleusercontent.com/datasets/PromptCloudHQ/imdb-data"  # Asegúrate de descargar y colocar el archivo localmente
file_path = "imdb.csv"  # Cambia esto si el archivo tiene otro nombre
data = pd.read_csv(file_path)

# Validar el dataset
def validate_dataset(df):
    report = {}

    # Revisar valores nulos
    report['missing_values'] = df.isnull().sum().to_dict()

    # Revisar duplicados
    report['duplicates'] = df.duplicated().sum()

    # Revisar longitudes mínimas de texto en columnas clave
    if 'Title' in df.columns:
        report['short_titles'] = (df['Title'].str.len() < 2).sum()
    if 'Description' in df.columns:
        report['short_descriptions'] = (df['Description'].str.len() < 10).sum()

    # Revisar géneros inválidos (simples ejemplos de validación)
    if 'Genre' in df.columns:
        valid_genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Thriller', 'Romance', 'Adventure', 'Sci-Fi', 'Fantasy']
        report['invalid_genres'] = df['Genre'].apply(lambda x: all(g.strip() not in valid_genres for g in x.split(',')) if pd.notnull(x) else False).sum()

    return report

validation_report = validate_dataset(data)
print("Informe de validación del dataset:")
for key, value in validation_report.items():
    print(f"{key}: {value}")

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
