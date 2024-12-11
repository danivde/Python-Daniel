
# 1. Crear una tupla e intentar modificar su contenido
mi_tupla = (1, 2, 3)

# Intentar modificar un elemento de la tupla
try:
    mi_tupla[0] = 10  # Intentamos cambiar el primer elemento
except TypeError as e:
    print(f"Error: {e}")  # Capturamos y mostramos el error

# 2. Crear una tupla mixta con diferentes tipos de datos
tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

# Imprimir la tupla mixta
print("\nTupla Mixta:")
print(tupla_mixta)

# 3. Modificar el contenido del tercer elemento de la tupla (una lista)
try:
    tupla_mixta[2][0] = 10  # Modificar el primer elemento de la lista dentro de la tupla
except TypeError as e:
    print(f"Error al modificar: {e}")  # Capturamos cualquier error que ocurra

# Imprimir la tupla mixta después de la modificación
print("\nTupla después de la modificación del tercer elemento:")
print(tupla_mixta)

# 4. Imprimir los elementos de la tupla con su tipo
print("\nImpresión de los elementos con su tipo:")
for elemento in tupla_mixta:
    print(f"{elemento} => {str(type(elemento))}")

# 5. Convertir la tupla en una lista, modificar un elemento y volver a convertirla en tupla
lista_mixta = list(tupla_mixta)  # Convertir la tupla en una lista

# Modificar el elemento 1 (que es la cadena "dos")
lista_mixta[1] = "tres"

# Convertir la lista de nuevo a tupla
tupla_mixta_modificada = tuple(lista_mixta)

# Imprimir la nueva tupla
print("\nTupla después de modificar el elemento 1 (de 'dos' a 'tres'):")
print(tupla_mixta_modificada)

# 6. Crear una tupla numérica y realizar operaciones de suma, máximo y mínimo
tupla_numerica = (10, 20, 30, 40, 50)

# Realizar operaciones sobre la tupla
suma = sum(tupla_numerica)
maximo = max(tupla_numerica)
minimo = min(tupla_numerica)

# Imprimir los resultados de las operaciones
print("\nOperaciones con tupla numérica:")
print(f"Suma: {suma}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# 7. Calcular los cuadrados de los elementos de la tupla usando una comprensión de tuplas
cuadrados = tuple(x**2 for x in tupla_numerica)

# Imprimir la tupla de cuadrados
print("\nCuadrados de los elementos de la tupla:")
print(cuadrados)

# 8. Desempaquetar la tupla en tantas variables como elementos tenga
a, b, c, d, e = tupla_numerica

# Imprimir las variables desempaquetadas
print("\nDesempaquetado de la tupla numérica:")
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")
