from NewCrud.loadout.equipamentos.letais.explosivos.explosive import Explosive


class C4(Explosive):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(name, design, description, area_of_effect, damage)

    # Polimorfismo de sobreposicao. 
    def activate(self):

        print('Explosão')
        self.make_noise()

    # Polimorfismo de sobreposicao. 
    def make_noise(self):
        print('Explosão barulho')