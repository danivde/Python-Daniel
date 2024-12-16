from flask import Flask, request, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Diccionario vacío para almacenar las películas
peliculas = {}

# Ruta para añadir una película
@app.route('/api/peliculas', methods=['POST'])
def añadir_pelicula():
    data = request.get_json()  # Obtener los datos en formato JSON

    nombre = data.get('nombre')
    director = data.get('director')
    año = data.get('año')
    presupuesto = data.get('presupuesto')

    if nombre in peliculas:
        return jsonify({"error": "¡La película ya está en la lista!"}), 400

    peliculas[nombre] = {
        "director": director,
        "año": año,
        "presupuesto": presupuesto
    }
    
    return jsonify({"message": f"La película '{nombre}' ha sido añadida."}), 201

# Ruta para eliminar una película
@app.route('/api/peliculas/<string:nombre>', methods=['DELETE'])
def eliminar_pelicula(nombre):
    if nombre in peliculas:
        del peliculas[nombre]
        return jsonify({"message": f"La película '{nombre}' ha sido eliminada."}), 200
    else:
        return jsonify({"error": "¡La película no está en la lista!"}), 404

# Ruta para mostrar todas las películas
@app.route('/api/peliculas', methods=['GET'])
def mostrar_peliculas():
    if peliculas:
        return jsonify(peliculas), 200
    else:
        return jsonify({"message": "No hay películas en la lista."}), 404

# Ruta para modificar los metadatos de una película
@app.route('/api/peliculas/<string:nombre>', methods=['PUT'])
def modificar_pelicula(nombre):
    if nombre not in peliculas:
        return jsonify({"error": "¡La película no está en la lista!"}), 404

    data = request.get_json()
    director = data.get('director', peliculas[nombre]['director'])
    año = data.get('año', peliculas[nombre]['año'])
    presupuesto = data.get('presupuesto', peliculas[nombre]['presupuesto'])

    peliculas[nombre] = {
        "director": director,
        "año": año,
        "presupuesto": presupuesto
    }

    return jsonify({"message": f"Los metadatos de '{nombre}' han sido actualizados."}), 200

# Ruta para buscar una película
@app.route('/api/peliculas/buscar/<string:nombre>', methods=['GET'])
def buscar_pelicula(nombre):
    if nombre in peliculas:
        return jsonify(peliculas[nombre]), 200
    else:
        return jsonify({"error": f"La película '{nombre}' no está en la lista."}), 404

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
