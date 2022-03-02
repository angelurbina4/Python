from Mascota import Mascota
from Ninja import Ninja
from Perrito import Perrito

lilo = Mascota("Lilo", "Perro", "Galletas", 100, 100)

angel = Ninja("angel", "urbina", lilo, "galletas", "zanahorias")

angel.bañar().caminar().alimentar()

luna = Perrito("Luna", "Perro", "Galletas", 100, 100, "salchicha")

winston = Ninja("Winston", "Mendez", luna, "galletas", "zanahorias")

winston.bañar().alimentar()

venus = Perrito("Venus", "Perro", "Galletas", 100, 100, "Bulldog")


Perrito.imprimePerritos()

Mascota.imprimeMascotas()
