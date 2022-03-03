class CuentaBancaria:
    
    listaCuentaBancarias = []
    def __init__(self, tasa_int,  balance = 0):
        self.tasa_int = tasa_int/100
        self.balance = balance
        CuentaBancaria.listaCuentaBancarias.append(self)
    
    def deposito(self, monto):
        self.balance += monto
        return self
    
    def retiro(self, monto):
        if self.saldo(self, monto,):
            self.balance -= monto
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}, Tasa de interes: {self.tasa_int*100}%")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_int
        return self
    
    @staticmethod
    def saldo(self, monto):
        if (self.balance - monto) < 0:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return False
        else:
            return True
    
    @classmethod
    def mostrar_lista(cls):
        for cuenta in cls.listaCuentaBancarias:
            cuenta.mostrar_info_cuenta()