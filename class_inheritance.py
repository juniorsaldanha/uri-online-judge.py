class Animal():
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.donoName = dono

    def correr(self):
        print(f'{self.nome} está correndo')

    def brincar(self):
        print(f'{self.nome} está brincando')

    def comer(self):
        print(f'{self.nome} está comendo')

    def dono(self):
        print(f"{self.donoName} é o dono do {self.nome}")


class Cachorro(Animal):
    def __init__(self, nome, dono):
        super().__init__(nome, 'Cachorro', dono)
    
    def latir(self):
        print(f'{self.nome} está latindo')

class Pug(Cachorro):
    def __init__(self, nome, dono):
        super().__init__(nome, dono)

    def roncar(self):
        print(f"Roncar, pq Pug ronca kkk")
    
class Peixe(Animal):
    def __init__(self, nome, dono):
        super().__init__(nome, 'Peixe', dono)

    def nadar(self):
        print(f'{self.nome} está nadando')

    def correr(self):
        pass

px = Peixe("Peixin","Evandro")
px.nadar()
px.correr()
px.comer()
px.dono()

print()

ch = Cachorro("Cachorrin", "Junior")
ch.correr()
ch.latir()
ch.comer()
ch.dono()
print()

pug = Pug("Puggin", "Junior Saldanha")
pug.roncar()
pug.correr()
pug.comer()
pug.latir()
pug.dono()