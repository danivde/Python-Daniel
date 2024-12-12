# Diccionario vacío para almacenar las películas
peliculas = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n Menú de Gestión de Películas ")
    print("1. Añadir Película")
    print("2. Eliminar Película")
    print("3. Mostrar Lista de Películas")
    print("4. Modificar Película")
    print("5. Buscar Película")
    print("6. Salir")

# Función para añadir una película
def añadir_pelicula():
    pelicula = input("Introduce el nombre de la película a añadir: ").strip()
    if pelicula in peliculas:
        print("¡La película ya está en la lista!")
    else:
        director = input("Introduce el nombre del director: ").strip()
        año = input("Introduce el año de la película: ").strip()
        presupuesto = input("Introduce el presupuesto de la película en millones de euros: ").strip()

        # Validar que los valores de año y presupuesto son números
        try:
            año = int(año)
        except ValueError :
            Print ("El año debe ser un número entero")
            presupuesto = float(presupuesto)
        except ValueError:
            print("El año debe ser un número entero y el presupuesto un número decimal.")
            return

        # Guardamos la película en el diccionario
        peliculas[pelicula] = {'director': director, 'año': año, 'presupuesto': presupuesto}
        print(f"La película '{pelicula}' ha sido añadida.")

# Función para eliminar una película
def eliminar_pelicula():
    pelicula = input("Introduce el nombre de la película a eliminar: ").strip()
    if pelicula in peliculas:
        del peliculas[pelicula]
        print(f"La película '{pelicula}' ha sido eliminada.")
    else:
        print("¡La película no está en la lista!")

# Función para mostrar todas las películas
def mostrar_peliculas():
    if peliculas:
        print("\nLista de Películas:")
        for pelicula, metadatos in peliculas.items():
            print(f"- {pelicula}")
            print(f"  Director: {metadatos['director']}, Año: {metadatos['año']}, Presupuesto en millones de euros: {metadatos['presupuesto ']}")
    else:
        print("No hay películas en la lista.")

# Función para modificar una película
def modificar_pelicula():
    pelicula = input("Introduce el nombre de la película que deseas modificar: ").strip()
    if pelicula in peliculas:
        print(f"Modificar los metadatos de la película '{pelicula}':")
        director = input(f"Nuevo director (actual: {peliculas[pelicula]['director']}): ").strip()
        año = input(f"Nuevo año (actual: {peliculas[pelicula]['año']}): ").strip()
        presupuesto = input(f"Nuevo presupuesto (actual: {peliculas[pelicula]['presupuesto']}): ").strip()

        # Validar año y presupuesto
        try:
            if año:
                año = int(año)
            else:
                año = peliculas[pelicula]['año']  # Mantener el valor actual si no se ingresa nada

            if presupuesto:
                presupuesto = float(presupuesto)
            else:
                presupuesto = peliculas[pelicula]['presupuesto']  # Mantener el valor actual si no se ingresa nada

        except ValueError:
            print("El año debe ser un número entero y el presupuesto un número decimal.")
            return
        
        # Actualizamos los metadatos
        peliculas[pelicula] = {'director': director, 'año': año, 'presupuesto': presupuesto}
        print(f"Los metadatos de '{pelicula}' han sido actualizados.")
    else:
        print("¡La película no está en la lista!")

# Función para buscar una película
def buscar_pelicula():
    pelicula = input("Introduce el nombre de la película que deseas buscar: ").strip()
    if pelicula in peliculas:
        print(f"La película '{pelicula}' está en la lista.")
        print(f"  Director: {peliculas[pelicula]['director']}, Año: {peliculas[pelicula]['año']}, Presupuesto: {peliculas[pelicula]['presupuesto en millones']}")
    else:
        print(f"La película '{pelicula}' no está en la lista.")

# Función principal que controla el flujo del programa
def gestionar_peliculas():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-6): "))
            
            if opcion == 1:
                añadir_pelicula()
            elif opcion == 2:
                eliminar_pelicula()
            elif opcion == 3:
                mostrar_peliculas()
            elif opcion == 4:
                modificar_pelicula()
            elif opcion == 5:
                buscar_pelicula()
            elif opcion == 6:
                print("¡Gracias por usar el gestor de películas!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el programa
gestionar_peliculas()
