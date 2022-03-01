class User:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.pesos = 0

    def hacer_retiro(self, cantidad):
        self.pesos -= cantidad

    def hacer_deposito(self, cantidad):
        self.pesos += cantidad

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: {self.pesos}")

    def transferir_dinero(self, otro_usuario, cantidad):
        self.pesos -= cantidad
        otro_usuario.pesos += cantidad