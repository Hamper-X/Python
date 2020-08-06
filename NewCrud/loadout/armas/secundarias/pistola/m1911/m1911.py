import os

from PROJETO_FINAL.codigo.loadout.armas.secundarias.pistolas.pistol import Pistol


class M1911(Pistol):

pistolSound = os.path.join(os.getcwd(), 'loadout', 'armas', 'secundarias', 'pistolas', 'm1911', '1911.mp3')

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
        print('Atirando com a M1911')
        self.make_noise(self.AUDIO_FILE_PATH)

    """
        @Acoes:
            Sobrescrevendo o metodo "reload( )" da classe Weapon, ou seja
            estou realiza um polimorfismo de sobreposicao (override)
    """
    def reload(self):
        print('Animação de carregamento da M1911')