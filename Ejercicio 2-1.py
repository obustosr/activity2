class Persona:
    def __init__(self, nombre: str, apellido: str, numero_documento: str, anio_nacimiento: int):
        
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self) -> None:
       
        print(f"Nombre completo : {self.nombre} {self.apellido}")
        print(f"Documento       : {self.numero_documento}")
        print(f"Año nacimiento  : {self.anio_nacimiento}")
        print("-" * 30)


def main():
    
    persona1 = Persona("Carlos", "Gómez", "1023456789", 1995)
    persona2 = Persona("Mariana", "Zapata", "987654321", 2001)

    
    print("--- Datos Persona 1 ---")
    persona1.imprimir()

    print("--- Datos Persona 2 ---")
    persona2.imprimir()


if __name__ == "__main__":
    main()