import requests
import json

# URL de la API
api_url = "https://www.kaggle.com/datasets/karakaggle/kaggle-cat-vs-dog-dataset"  # Cambia esto por la URL de tu API

# Hacer la solicitud a la API
response = requests.get(api_url)

if response.status_code == 200:  # Verificar que la solicitud fue exitosa
    data = response.json()  # Convertir la respuesta a un diccionario Python

    # Guardar los datos en un archivo JSON
    with open("api_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Datos guardados exitosamente en api_data.json")
else:
    print(f"Error al obtener los datos. Código de estado: {response.status_code}")