class Persona:
    def __init__(
        self,
        nombre: str,
        apellido: str,
        numero_documento: str,
        anio_nacimiento: int,
        pais_nacimiento: str,
        genero: str,
    ):

        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento

    
        genero_upper = genero.upper()
        if genero_upper not in ('H', 'M'):
            raise ValueError("El género debe ser 'H' (Hombre) o 'M' (Mujer).")
        self.genero = genero_upper

    def imprimir(self) -> None:
        """Muestra en pantalla todos los valores de los atributos."""
        print(f"Nombre completo     : {self.nombre} {self.apellido}")
        print(f"Documento           : {self.numero_documento}")
        print(f"Año nacimiento      : {self.anio_nacimiento}")
        print(f"País de nacimiento  : {self.pais_nacimiento}")
        print(f"Género              : {'Hombre (H)' if self.genero == 'H' else 'Mujer (M)'}")
        print("-" * 35)


def main():

    persona1 = Persona(
        nombre="Carlos",
        apellido="Gómez",
        numero_documento="1023456789",
        anio_nacimiento=1995,
        pais_nacimiento="Colombia",
        genero="H",
    )

    persona2 = Persona(
        nombre="Mariana",
        apellido="Zapata",
        numero_documento="987654321",
        anio_nacimiento=2001,
        pais_nacimiento="Argentina",
        genero="M",
    )

    print("--- Datos Persona 1 ---")
    persona1.imprimir()

    print("--- Datos Persona 2 ---")
    persona2.imprimir()


if __name__ == "__main__":
    main()