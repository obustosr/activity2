from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = "gasolina"
    BIOETANOL = "bioetanol"
    DIESEL = "diésel"
    BIODIESEL = "biodiésel"
    GAS_NATURAL = "gas natural"


class TipoAutomovil(Enum):
    CARRO_CIUDAD = "carro de ciudad"
    SUBCOMPACTO = "subcompacto"
    COMPACTO = "compacto"
    FAMILIAR = "familiar"
    EJECUTIVO = "ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "blanco"
    NEGRO = "negro"
    ROJO = "rojo"
    NARANJA = "naranja"
    AMARILLO = "amarillo"
    VERDE = "verde"
    AZUL = "azul"
    VIOLETA = "violeta"


class Automovil:
    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: float,
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: float,
        color: Color,
        velocidad_actual: float = 0.0,
    ):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = velocidad_actual

    def get_marca(self) -> str:
        return self._marca

    def set_marca(self, marca: str) -> None:
        self._marca = marca

    def get_modelo(self) -> int:
        return self._modelo

    def set_modelo(self, modelo: int) -> None:
        self._modelo = modelo

    def get_motor(self) -> float:
        return self._motor

    def set_motor(self, motor: float) -> None:
        self._motor = motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self._tipo_combustible = tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self._tipo_automovil

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self._tipo_automovil = tipo_automovil

    def get_numero_puertas(self) -> int:
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self._numero_puertas = numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self._cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self._cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self) -> float:
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: float) -> None:
        self._velocidad_maxima = velocidad_maxima

    def get_color(self) -> Color:
        return self._color

    def set_color(self, color: Color) -> None:
        self._color = color

    def get_velocidad_actual(self) -> float:
        return self._velocidad_actual

    def set_velocidad_actual(self, velocidad_actual: float) -> None:
        self._velocidad_actual = velocidad_actual

    def acelerar(self, incremento: float) -> None:
        if self._velocidad_actual + incremento > self._velocidad_maxima:
            print(f"No se puede acelerar a {self._velocidad_actual + incremento} km/h. Supera la velocidad máxima permitida de {self._velocidad_maxima} km/h.")
        else:
            self._velocidad_actual += incremento

    def desacelerar(self, decremento: float) -> None:
        if self._velocidad_actual - decremento < 0:
            print(f"No se puede desacelerar a {self._velocidad_actual - decremento} km/h. No es posible tener una velocidad negativa.")
        else:
            self._velocidad_actual -= decremento

    def frenar(self) -> None:
        self._velocidad_actual = 0.0

    def calcular_tiempo_llegada(self, distancia_km: float) -> float:
        if self._velocidad_actual == 0:
            return float("inf")
        return distancia_km / self._velocidad_actual

    def mostrar_atributos(self) -> None:
        print(f"Marca               : {self._marca}")
        print(f"Modelo (año)        : {self._modelo}")
        print(f"Motor               : {self._motor} L")
        print(f"Tipo de combustible : {self._tipo_combustible.value}")
        print(f"Tipo de automóvil   : {self._tipo_automovil.value}")
        print(f"Número de puertas   : {self._numero_puertas}")
        print(f"Cantidad de asientos: {self._cantidad_asientos}")
        print(f"Velocidad máxima    : {self._velocidad_maxima} km/h")
        print(f"Color               : {self._color.value}")
        print(f"Velocidad actual    : {self._velocidad_actual} km/h")


def main():
    auto = Automovil(
        marca="Toyota",
        modelo=2024,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.COMPACTO,
        numero_puertas=4,
        cantidad_asientos=5,
        velocidad_maxima=180.0,
        color=Color.ROJO,
        velocidad_actual=0.0,
    )

    auto.mostrar_atributos()

    auto.set_velocidad_actual(100.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(20.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.desacelerar(50.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.frenar()
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")


if __name__ == "__main__":
    main()