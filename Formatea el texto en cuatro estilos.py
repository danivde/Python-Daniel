# Formatea el texto en cuatro estilos
def messageFormatter(texto, tipo):
    if tipo == 'info': 
        return '\033[44m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'warning': 
        return '\033[43m\033[31m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'error':
        return '\033[41m' + ' ' + texto + ' ' + '\033[0m' 
    if tipo == 'success': 
        return '\033[42m' + ' ' + texto + ' ' + '\033[0m' 
    
    return '\033[0m' + ' ' + texto + ' ' + '\033[0m'
    

    # Definimos __name__ como __main__  
if __name__ == "__main__":  
    
    if len(sys.argv) < 3:  # Comprueba si se pasaron menos de 2 argumentos adicionales.
        print(f"Uso: {os.path.basename(__file__)} texto tipo")
        print("Este script necesita al menos 2 argumentos para funcionar correctamente. EL primer argumento es el texto a destacar, el segundo es el tipo (info, error, warning, success)")
    else:
        print(messageFormatter(sys.argv[1], sys.argv[2]))

        