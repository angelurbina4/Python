from Mascota import Mascota

class Perrito(Mascota):
    
    listaPerritos = []
    
    def __init__(self, name, tipo, golosinas, salud, energia, raza):
        super().__init__(name, tipo, golosinas, salud, energia)
        self.raza = raza
        Perrito.listaPerritos.append(self)

    @classmethod
    def imprimePerritos(cls):
        for perrito in cls.listaPerritos:
            perrito.imprime()

    def imprime(self):
        super().imprime()
        print(f"Raza: {self.raza}")
