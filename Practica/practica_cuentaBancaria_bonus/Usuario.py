from CuentaBancaria import CuentaBancaria


class Usuario:
    
    def __init__(self, nombre, email, cuentas):
        self.nombre = nombre
        self.email = email
        self.cuentas = {} #Bonus
        self.cuentas.update(cuentas) #BONUS
    
    def hacer_deposito(self, monto, cuenta):
        self.cuentas[cuenta].balance += monto
        return self
    
    def hacer_retiro(self, monto, cuenta):
        self.cuentas[cuenta].balance -= monto
        return self
    
    def mostar_balance(self, cuenta):
        print(f"El balance de {self.nombre} es de {self.cuentas[cuenta].balance}")
        return self
    
    def hacer_transferencia(self, otro_usario, cuenta_otro_usuario, monto, cuenta):
        self.cuentas[cuenta].balance -= monto
        otro_usario.cuentas[cuenta_otro_usuario].balance += monto
        return self
    
    
    