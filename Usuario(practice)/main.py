from User import User

john = User("John")
mary = User("Mary")

print(john.nombre)

john.hacer_deposito(1500)
john.hacer_retiro(100)

john.mostrar_balance_usuario()

mary.hacer_deposito(100)
mary.hacer_retiro(50)
mary.transferir_dinero(john, 20)
mary.mostrar_balance_usuario()

john.transferir_dinero(mary, 100)

print(john.pesos)
print(mary.pesos)