from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Diccionario vacío para almacenar las películas
peliculas: Dict[str, dict] = {}

# Modelo para recibir los datos de las películas a través de la API
class Pelicula(BaseModel):
    nombre: str
    director: str
    año: int
    presupuesto: float

# Ruta para añadir una nueva película
@app.post("/api/peliculas")
async def añadir_pelicula(pelicula: Pelicula):
    if pelicula.nombre in peliculas:
        raise HTTPException(status_code=400, detail="¡La película ya está en la lista!")
    
    peliculas[pelicula.nombre] = {
        "director": pelicula.director,
        "año": pelicula.año,
        "presupuesto": pelicula.presupuesto
    }
    return {"message": f"La película '{pelicula.nombre}' ha sido añadida."}

# Ruta para eliminar una película
@app.delete("/api/peliculas/{nombre}")
async def eliminar_pelicula(nombre: str):
    if nombre in peliculas:
        del peliculas[nombre]
        return {"message": f"La película '{nombre}' ha sido eliminada."}
    else:
        raise HTTPException(status_code=404, detail="¡La película no está en la lista!")

# Ruta para mostrar todas las películas
@app.get("/api/peliculas")
async def mostrar_peliculas():
    if peliculas:
        return peliculas
    else:
        raise HTTPException(status_code=404, detail="No hay películas en la lista.")

# Ruta para modificar los metadatos de una película
@app.put("/api/peliculas/{nombre}")
async def modificar_pelicula(nombre: str, pelicula: Pelicula):
    if nombre not in peliculas:
        raise HTTPException(status_code=404, detail="¡La película no está en la lista!")
    
    peliculas[nombre] = {
        "director": pelicula.director,
        "año": pelicula.año,
        "presupuesto": pelicula.presupuesto
    }
    return {"message": f"Los metadatos de '{nombre}' han sido actualizados."}

# Ruta para buscar una película
@app.get("/api/peliculas/buscar/{nombre}")
async def buscar_pelicula(nombre: str):
    if nombre in peliculas:
        return peliculas[nombre]
    else:
        raise HTTPException(status_code=404, detail=f"La película '{nombre}' no está en la lista.")
