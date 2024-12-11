#Simular un texto de 1000 líneas
texto_largo = ["Línea " + str(i + 1) for i in range(1000)]

# se crea una lista vacía para almecenar los bloques
Bloques_palabras = []

#crear bloques de 25 líneas
for i in range (0, len(texto_largo), 25):
    lista = texto_largo [i:i + 25]
    Bloques_palabras.append(lista)

#imprimir número de listas creadas
print (f"Se han creado {len(Bloques_palabras)} bloques de palabras.")

#imprimir la primera lista
print(Bloques_palabras [0])

