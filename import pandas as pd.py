import pandas as pd

def cargar_datos():
    """Carga un archivo CSV desde una URL en un DataFrame de Pandas."""
    url = 'https://drive.google.com/uc?export=download&id=1033_pgXO86pl9hwlIvGZZtNgmbiYJ7ps'
    try:
        df = pd.read_csv(url)
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Exploración del DataFrame
def explorar_dataframe(df):
    """Realiza una exploración básica del DataFrame."""
    print("\nPrimeras 5 filas del DataFrame:")
    print(df.head())
    
    print("\nÚltimas 5 filas del DataFrame:")
    print(df.tail())

    print("\nInformación general del DataFrame:")
    print(df.info())

    print("\nEstadísticas descriptivas:")
    print(df.describe())

# Enriquecer datos: Plantilla para agregar columnas (ejemplo básico)
def enriquecer_datos(df):
    """Agrega columnas con datos adicionales sobre el protagonista."""
    # Placeholder: Agregar columnas vacías para almacenar los datos del protagonista
    df['Protagonista'] = ""
    df['Sueldo_Protagonista'] = 0.0
    df['Nacimiento_Protagonista'] = 0
    df['Edad_Protagonista'] = 0

    # Aquí se podría implementar lógica para rellenar los datos (por ejemplo, usando una API externa)

    return df

# Análisis y relaciones
def analizar_relaciones(df):
    """Ejemplo de análisis: Relaciones entre género, rentabilidad y edad del protagonista."""
    if 'Genero' in df.columns and 'Rentabilidad' in df.columns:
        print("\nRelación entre género y rentabilidad:")
        rentabilidad_genero = df.groupby('Genero')['Rentabilidad'].mean()
        print(rentabilidad_genero)
    else:
        print("Columnas 'Genero' y 'Rentabilidad' no encontradas en el DataFrame.")

    # Más análisis pueden incluir correlaciones y visualizaciones

# Flujo principal
if __name__ == "__main__":
    df = cargar_datos()

    if df is not None:
        print(df.to_string(index=False))  # Imprime el DataFrame completo
        explorar_dataframe(df)
        df = enriquecer_datos(df)
        analizar_relaciones(df)
