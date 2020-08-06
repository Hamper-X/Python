from time import sleep
from NewCrud.loadout.equipamentos.letais.explosivos.explosive import Explosive


class FragGrenade(Explosive):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(name, design, description, area_of_effect, damage)

    # Polimorfismo de sobreposicao
    def activate(self):
        print('Granada ativada...')

        #Considerando tempo de 3 segundos antes da explosão
        x=3
        for i in range(3):
            sleep(i)
            print(f'explosao em {x}...')
            x = x-1

        print('Animação Explosão ...')
        self.make_noise()

    # Polimorfismo de sobreposicao
    def make_noise(self):
        print('Barulho Explosão')