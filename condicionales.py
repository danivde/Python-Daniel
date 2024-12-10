# Intentar pedir al usuario que ingrese un número
try:
    numero = float(input("Ingresa un número: "))
    
    # Usar condicionales para verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
    
   
    if True:  
        print("El número es verdadero")

    if False:  
        print("El número es falso.")
        
except ValueError:
   #por si el usuario escribe una letra en vez de un número
    print("Error: Debes ingresar un número válido.")

