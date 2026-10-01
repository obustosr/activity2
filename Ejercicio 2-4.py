import math


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.hypot(self.base, self.altura)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if math.isclose(self.base, self.altura) and math.isclose(self.altura, hipotenusa):
            return "Equilátero"
        elif (
            math.isclose(self.base, self.altura)
            or math.isclose(self.base, hipotenusa)
            or math.isclose(self.altura, hipotenusa)
        ):
            return "Isósceles"
        else:
            return "Escaleno"


def main():
    circulo = Circulo(5.0)
    rectangulo = Rectangulo(4.0, 6.0)
    cuadrado = Cuadrado(4.0)
    triangulo = TrianguloRectangulo(3.0, 4.0)

    print(f"Círculo:")
    print(f"  Área: {circulo.calcular_area():.2f} cm²")
    print(f"  Perímetro: {circulo.calcular_perimetro():.2f} cm\n")

    print(f"Rectángulo:")
    print(f"  Área: {rectangulo.calcular_area():.2f} cm²")
    print(f"  Perímetro: {rectangulo.calcular_perimetro():.2f} cm\n")

    print(f"Cuadrado:")
    print(f"  Área: {cuadrado.calcular_area():.2f} cm²")
    print(f"  Perímetro: {cuadrado.calcular_perimetro():.2f} cm\n")

    print(f"Triángulo Rectángulo:")
    print(f"  Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"  Área: {triangulo.calcular_area():.2f} cm²")
    print(f"  Perímetro: {triangulo.calcular_perimetro():.2f} cm")
    print(f"  Tipo: {triangulo.determinar_tipo_triangulo()}")


if __name__ == "__main__":
    main()