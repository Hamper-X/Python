from PROJETO_FINAL.codigo.loadout.equipamentos.letais.lethal_equipment import LethalEquipment


#A classe "Explosive" é do tipo da classe "EquipamentoLetal"
class Explosive(LethalEquipment):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(
            name=name, design=design, description=description,
            area_of_effect=area_of_effect, damage=damage)

    def explode(self):
        print('Animação Explosão')
        self.make_noise()

    def make_noise(self):
        print('Som Explosão')