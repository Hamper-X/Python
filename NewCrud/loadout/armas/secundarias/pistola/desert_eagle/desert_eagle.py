import os

from NewCrud.loadout.armas.secundarias.pistolas.pistol import Pistol


class DesertEagle(Pistol):

    pistolSound = os.path.join(os.getcwd(), 'loadout', 'armas', 'secundarias', 'pistolas', 'desert_eagle', 'desert.mp3')

    #init com classe super, usando de polimorfismo para aderir a classe desertEagle dados da "pistol"
    def __init__(
            self, name, accuracy, damage, reload_speed, ammunition, muzzle='Default', barrel='Default',
            laser=False,  optic=None, dual=False):

        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic, dual=dual)


    """
        @Acoes:
            Sobrescrevendo o metodo "fire( )" da classe Weapon, ou seja
            estou realiza um polimorfismo de sobreposicao (override)
    """
    def fire(self):
        print('Atirando com a Desert Eagle')
        self.make_noise(self.pistolSound)

    """
        @Acoes:
            Sobrescrevendo o metodo "reload( )" da classe Weapon, ou seja
            estou realiza um polimorfismo de sobreposicao (override)
    """
    def reload(self):
        print('Animação de carregamento da Desert Eagle')