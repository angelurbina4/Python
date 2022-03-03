from Usuario import Usuario
from CuentaBancaria import CuentaBancaria

# john = Usuario("John", "john@email.com")
# print(john.balance)
# john.hacer_deposito(100)
# print(john.balance)
# john.hacer_retiro(50)
# print(john.balance)
# print("--------------")

#Bonus
carmen = Usuario("Carmen", "Carmen@email.com", {"cuenta_corriente": CuentaBancaria(10, 100)})
lilo = Usuario("Lilo", "lilo@email.com", {"cuenta_corriente": CuentaBancaria(10, 100), "cuenta_ahorro" : CuentaBancaria(3, 200)})

print(carmen)

carmen.hacer_deposito(100, "cuenta_corriente").mostar_balance("cuenta_corriente")
carmen.hacer_transferencia(lilo, "cuenta_corriente", 100, "cuenta_corriente")
carmen.mostar_balance("cuenta_corriente")
lilo.mostar_balance("cuenta_corriente")


# carmen.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).mostar_balance()
# print("--------------")
# lilo.hacer_deposito(100).hacer_deposito(100).hacer_retiro(200).mostar_balance()
# print("--------------")
# carmen.hacer_transferencia(lilo,100).mostar_balance()
# lilo.mostar_balance()
# print("--------------")


# cuenta = CuentaBancaria(10, 100)
# cuenta1 = CuentaBancaria(20)
# cuenta.deposito(100).deposito(100).deposito(100).retiro(50).generar_interes().mostrar_info_cuenta()
# cuenta1.deposito(200).deposito(300).retiro(50).retiro(50).retiro(50).retiro(50).generar_interes().mostrar_info_cuenta()
# print("--------")
# CuentaBancaria.mostrar_lista()


