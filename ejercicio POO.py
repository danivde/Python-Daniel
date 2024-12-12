from abc import ABC, abstractmethod

# Clase Persona (Clase Padre)
class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal  # Atributo privado
    
    @property
    def id_fiscal(self):
        return self.__id_fiscal
    
    @id_fiscal.setter
    def id_fiscal(self, value):
        self.__id_fiscal = value
    
    @abstractmethod
    def saludar(self):
        pass

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - ID Fiscal: {self.__id_fiscal}"
    
    def __del__(self):
        print(f"Persona {self.nombre} {self.apellidos} eliminada")

# Clase Cliente (Hija de Persona)
class Cliente(Persona):
    contador_clientes = 0  # Variable estática
    
    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, value):
        self.__id_cliente = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    @staticmethod
    def clientes_creados():
        return Cliente.contador_clientes

    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellidos}, mi correo es {self.email}"

    def __str__(self):
        return f"Cliente ID: {self.id_cliente} - {super().__str__()}"

    def __del__(self):
        print(f"Cliente id: {self.id_cliente} eliminado")
        Cliente.contador_clientes -= 1

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id_fiscal == other.id_fiscal
        return False

# Clase Factura
class Factura:
    def __init__(self, id_factura, cliente):
        self.id_factura = id_factura
        if isinstance(cliente, Cliente):
            self.cliente = cliente
        else:
            raise ValueError("El cliente debe ser una instancia de la clase Cliente.")
    
    @property
    def id_factura(self):
        return self.__id_factura
    
    @id_factura.setter
    def id_factura(self, value):
        self.__id_factura = value
    
    def __str__(self):
        return f"Factura ID: {self.id_factura} - {self.cliente}"
    
    def __eq__(self, other):
        if isinstance(other, Factura):
            return self.id_factura == other.id_factura and self.cliente == other.cliente
        return False

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Elián", "Torvalds", "98765432Z", 1, "elian.torvalds@example.com")
    cliente2 = Cliente("Zara", "Echandía", "45678901Y", 2, "zara.echandia@example.com")
    cliente3 = Cliente("Elián", "Torvalds", "98765432Z", 3, "elian.torvalds2@example.com")

    print(cliente1.saludar())
    print(cliente2.saludar())
    print(cliente3.saludar())

    factura1 = Factura(201, cliente1)
    factura2 = Factura(202, cliente2)
    factura3 = Factura(201, cliente1)

    print(factura1)
    print(factura2)
    print(factura3)

    print(f"Clientes creados: {Cliente.clientes_creados()}")

    # Comparación de objetos
    print(f"cliente1 == cliente3: {cliente1 == cliente3}")
    print(f"factura1 == factura3: {factura1 == factura3}")

    del cliente1
    del cliente2
    del cliente3

    print(f"Clientes creados después de eliminar: {Cliente.clientes_creados()}")
