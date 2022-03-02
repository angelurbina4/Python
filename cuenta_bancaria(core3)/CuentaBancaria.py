class CuentaBancaria:
    nombre_banco = "Banco Dojo"
    lista_cuentas = []
    
    def __init__(self, tasa_int, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)

    def hacer_retiro(self, cantidad, cta_debitar):
        if CuentaBancaria.puede_retirar(self.balance, cantidad):
            self.balance -= cantidad
        else: 
            print("Su balance no es suficiente para realizar esta transaccion")
        return self

    def hacer_deposito(self, cantidad):
        self.balance += cantidad
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * (self.tasa_int/100)
        else:
            print("Balanca negativo")
        return self

    @classmethod
    def cambio_banco(cls, nombre):
        cls.nombre_banco = nombre

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            cuenta.mostrar_balance_usuario()

    def mostrar_balance_usuario(self):
        print(f"Tasa: {self.tasa_int}, Balance: {self.balance}")
        return self

    def transfer_dinero(self, usuario, cantidad, cta_creditar):
        if CuentaBancaria.puede_retirar(self.balance, cantidad):
            self.balance -= cantidad
            usuario.cuentas[cta_creditar].balance += cantidad
        else:
            print("Su balance no es suficiente para realizar esta transaccion")

    @staticmethod
    def puede_retirar(balance, cantidad_retirar):
        if (balance - cantidad_retirar) < 0:
            return False
        else:
            return True