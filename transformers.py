from transformers import pipeline
import gradio as gr

# Cargar un pipeline de Hugging Face con un modelo BERT para análisis de sentimiento
model = pipeline("sentiment-analysis")

def predict_sentiment(text):
    # Obtener el resultado del modelo
    result = model(text)
    # Extraer la etiqueta y la confianza del resultado
    label = result[0]['label']
    confidence = round(result[0]['score'], 4)
    return {label: confidence}

# Crear una interfaz de Gradio
iface = gr.Interface(fn=predict_sentiment, inputs="text", outputs="json")

# Lanzar la interfaz
iface.launch()

