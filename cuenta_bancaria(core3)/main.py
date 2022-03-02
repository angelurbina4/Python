from User import User
from CuentaBancaria import CuentaBancaria

lilo = User("Lilo")
cynthia = User("Cynthia")

lilo.cuentas["cta_corriente"].transfer_dinero(cynthia, 50, "cta_corriente")
print(lilo.cuentas["cta_corriente"].balance)
# cuenta1 = CuentaBancaria(10, 200)
# cuenta2 = CuentaBancaria(4, 500)
# cuenta1.hacer_deposito(100).hacer_deposito(50).hacer_deposito(150).hacer_retiro(100).generar_interes().mostrar_balance_usuario()
# cuenta2.hacer_deposito(200).hacer_deposito(200).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).generar_interes().mostrar_balance_usuario()

# CuentaBancaria.imprimir_cuentas()

