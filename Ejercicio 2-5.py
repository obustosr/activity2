from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:
    def __init__(
        self,
        nombres_titular: str,
        apellidos_titular: str,
        numero_cuenta: str,
        tipo_cuenta: TipoCuenta,
    ):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self) -> None:
        print(f"Titular        : {self.nombres_titular} {self.apellidos_titular}")
        print(f"Número cuenta  : {self.numero_cuenta}")
        print(f"Tipo de cuenta : {self.tipo_cuenta.value}")
        print(f"Saldo actual   : ${self.saldo:,.2f}")
        print("-" * 35)

    def consultar_saldo(self) -> float:
        return self.saldo

    def consignar(self, valor: float) -> None:
        if valor <= 0:
            print("El valor a consignar debe ser mayor que cero.")
            return
        self.saldo += valor
        print(f"Consignación exitosa: ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")

    def retirar(self, valor: float) -> None:
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
        elif valor > self.saldo:
            print(f"Fondos insuficientes. Intenta retirar ${valor:,.2f} pero el saldo es ${self.saldo:,.2f}.")
        else:
            self.saldo -= valor
            print(f"Retiro exitoso: ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")


def main():
    cuenta = CuentaBancaria(
        nombres_titular="Juan",
        apellidos_titular="Pérez",
        numero_cuenta="1234567890",
        tipo_cuenta=TipoCuenta.AHORROS,
    )

    cuenta.imprimir()
    cuenta.consignar(100000.0)
    print(f"Consulta de saldo: ${cuenta.consultar_saldo():,.2f}")
    cuenta.retirar(40000.0)
    cuenta.retirar(80000.0)
    cuenta.imprimir()


if __name__ == "__main__":
    main()