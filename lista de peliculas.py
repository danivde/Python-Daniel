#lista de peliculas
# Lista vacía para almacenar las películas
peliculas = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Gestión de Películas ---")
    print("1. Añadir Película")
    print("2. Eliminar Película")
    print("3. Mostrar Lista de Películas")
    print("4. Buscar Película")
    print("5. Salir")
    
# Función para añadir una película
def añadir_pelicula():
    pelicula = input("Introduce el nombre de la película a añadir: ").strip()
    if pelicula in peliculas:
        print("¡La película ya está en la lista!")
    else:
        peliculas.append(pelicula)
        print(f"La película '{pelicula}' ha sido añadida.")

# Función para eliminar una película
def eliminar_pelicula():
    pelicula = input("Introduce el nombre de la película a eliminar: ").strip()
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"La película '{pelicula}' ha sido eliminada.")
    else:
        print("¡La película no está en la lista!")

# Función para mostrar todas las películas
def mostrar_peliculas():
    if peliculas:
        print("\nLista de Películas:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")

# Función para buscar una película
def buscar_pelicula():
    pelicula = input("Introduce el nombre de la película que deseas buscar: ").strip()
    if pelicula in peliculas:
        print(f"La película '{pelicula}' está en la lista.")
    else:
        print(f"La película '{pelicula}' no está en la lista.")

# Función principal que controla el flujo del programa
def gestionar_peliculas():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            
            if opcion == 1:
                añadir_pelicula()
            elif opcion == 2:
                eliminar_pelicula()
            elif opcion == 3:
                mostrar_peliculas()
            elif opcion == 4:
                buscar_pelicula()
            elif opcion == 5:
                print("¡Gracias por usar el gestor de películas!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el programa
gestionar_peliculas()

