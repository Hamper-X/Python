import os
from NewCrud.loadout.equipamentos.taticos.tactical_equipment import TacticalEquipment

class FlashGrenade(TacticalEquipment):

    flashSound = os.path.join(os.getcwd(), 'loadout', 'equipamentos', 'taticos', 'flash', 'flash.mp3')

    def __init__(self, name, design, description, area_of_effect):
        super().__init__(name, design, description, area_of_effect)

    # Polimorfismo de sobreposicao. Estou fazendo a acao do equipamento especifico
    def activate(self):
        self.make_noise(self.flashSound)
        print('Cegando Inimigo.')