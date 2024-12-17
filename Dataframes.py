import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("datos_personas.csv")

# Parte 1: Exploración Básica del DataFrame

# Mostrar las primeras y últimas 5 filas
print("Primeras filas del DataFrame:")
print(df.head())
print("\nÚltimas filas del DataFrame:")
print(df.tail())

# Información general del DataFrame
print("\nInformación general del DataFrame:")
print(df.info())

# Estadísticas descriptivas básicas
print("\nEstadísticas descriptivas básicas:")
print(df.describe())

# Parte 2: Limpieza y Preparación de Datos

# Convertir altura de pulgadas a centímetros
df['altura_cm'] = df['altura_pulgadas'] * 2.54
print("\nPrimeras filas después de convertir la altura a centímetros:")
print(df[['altura_pulgadas', 'altura_cm']].head())

# Convertir peso de libras a kilogramos
df['peso_kg'] = df['peso_libras'] * 0.453592
print("\nPrimeras filas después de convertir el peso a kilogramos:")
print(df[['peso_libras', 'peso_kg']].head())

# Identificar valores faltantes
print("\nCantidad de valores faltantes por columna:")
print(df.isnull().sum())

# Rellenar valores faltantes con la media de la columna
df['altura_cm'] = df['altura_cm'].fillna(df['altura_cm'].mean())
df['peso_kg'] = df['peso_kg'].fillna(df['peso_kg'].mean())

# Mostrar las primeras filas después de rellenar los valores faltantes
print("\nPrimeras filas después de rellenar los valores faltantes:")
print(df.head())

# Parte 4: Operaciones Avanzadas

# Calcular percentiles del peso para cada género
percentiles_por_genero = df.groupby('género')['peso_kg'].quantile([0.25, 0.5, 0.75]).unstack()

print("\nPercentiles del peso para cada género:")
print(percentiles_por_genero)

# Calcular el IMC
df['IMC'] = df['peso_kg'] / (df['altura_cm'] / 100) ** 2

# Clasificar a los individuos según su IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo Peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso Normal'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

# Aplicar la clasificación del IMC
df['clasificacion_imc'] = df['IMC'].apply(clasificar_imc)

# Mostrar las primeras filas con la nueva clasificación
print("\nPrimeras filas después de clasificar por IMC:")
print(df[['peso_kg', 'altura_cm', 'IMC', 'clasificacion_imc']].head())

# Parte 5: Exportar Resultados

# Guardar los resultados del análisis en un nuevo archivo CSV
df.to_csv("resultados_analisis.csv", index=False)

print("\nLos resultados se han guardado en 'resultados_analisis.csv'")
