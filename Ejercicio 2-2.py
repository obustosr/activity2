from enum import Enum
from typing import Optional


class TipoPlaneta(Enum):

    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:

    UA_EN_MILLONES_KM: float = 149.597870

    def __init__(
        self,
        nombre: Optional[str] = None,
        cantidad_satelites: int = 0,
        masa: float = 0.0,
        volumen: float = 0.0,
        diametro: int = 0,
        distancia_media_sol: int = 0,
        tipo: TipoPlaneta = TipoPlaneta.TERRESTRE,
        es_observable: bool = False,
    ):
    
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen 
        self.diametro = diametro 
        self.distancia_media_sol = distancia_media_sol 
        self.tipo = tipo
        self.es_observable = es_observable

    def calcular_densidad(self) -> float:

        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:

        distancia_en_ua = self.distancia_media_sol / self.UA_EN_MILLONES_KM
        return distancia_en_ua > 3.4

    def imprimir(self) -> None:

        print(f"Nombre                      : {self.nombre}")
        print(f"Cantidad de satélites       : {self.cantidad_satelites}")
        print(f"Masa (kg)                   : {self.masa:.4e}")
        print(f"Volumen (km³)               : {self.volumen:.4e}")
        print(f"Diámetro (km)               : {self.diametro:,}")
        print(f"Distancia media al Sol (Mkm): {self.distancia_media_sol}")
        print(f"Tipo de planeta             : {self.tipo.value}")
        print(f"Observable a simple vista   : {'Sí' if self.es_observable else 'No'}")
        print(f"Densidad calculada (kg/km³) : {self.calcular_densidad():.4e}")
        print(f"Es planeta exterior         : {'Sí' if self.es_planeta_exterior() else 'No'}")
        print("-" * 50)


def main():

    jupiter = Planeta(
        nombre="Júpiter",
        cantidad_satelites=95,
        masa=1.898e27,
        volumen=1.43128e15,
        diametro=139820,
        distancia_media_sol=778,  
        tipo=TipoPlaneta.GASEOSO,
        es_observable=True,
    )

    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.972e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_media_sol=150, 
        tipo=TipoPlaneta.TERRESTRE,
        es_observable=True,
    )

    print("INFORMACIÓN DE LOS PLANETAS")
    jupiter.imprimir()
    tierra.imprimir()


if __name__ == "__main__":
    main()
