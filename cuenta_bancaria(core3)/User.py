from CuentaBancaria import CuentaBancaria
class User:
    
    def __init__(self, nombre ):
        self.nombre = nombre
        # self.cuenta = CuentaBancaria(5, 100)
        self.cuentas = {"cta_ahorro": CuentaBancaria(2, 50), "cta_corriente": CuentaBancaria(2, 200)}