class Mascota:
    listaMascotas = []
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        Mascota.listaMascotas.append(self)

    def dormir(self):
        self.energia += 25
        print(self.energia)
        return self
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        print(self.salud, self.energia)
        return self
    
    def jugar(self):
        self.salud += 5
        print(self.salud)
        return self
    
    def sonido(self):
        print("Muuu!")
        return self

    def imprime(self):
        print(f"Nombre: {self.name}")
        
    @classmethod
    def imprimeMascotas(cls):
        for mascota in cls.listaMascotas:
            mascota.imprime()