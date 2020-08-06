import os
import time
from NewCrud.loadout.armas.primarias.assault_rifle import AssaultRifle


class M4A1(AssaultRifle):

    m4Sound = os.path.join(os.getcwd(), 'loadout', 'armas', 'primarias', 'm4a1', 'm4.mp3')

    # init com a classe super, atribuindo assim os atributos de AssaultRifle
    def __init__(
            self, name, accuracy, damage, reload_speed, ammunition, muzzle='Default', barrel='Default',
            laser=False,  optic=None, stock='Default', underbarrel='Default'):

        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic, stock=stock, underbarrel=underbarrel)


    """
        @Acoes: Sobrescevendo o metodo fire() nativo da classe Weapon, realizando 
        assim, um polimorfismo de sobreposicao (override)
    """
    def fire(self):
        print('Atirando com a M4A1')
        self.make_noise(self.m4Sound)

    """
        @Acoes: Sobrescevendo o metodo reload() nativo da classe Weapon, realizando 
        assim, um polimorfismo de sobreposicao (override)
    """
    def reload(self):
        print('Recarregando AK47....')
        time.sleep(2)
        print('AK47 Carrregada')