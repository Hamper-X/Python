from NewCrud.loadout.equipamentos.equipment import Equipment


# LethalEquipment extende Equipment
class LethalEquipment(Equipment):
    def __init__(self, name, design, description, area_of_effect, damage):

        # Chamando o construtor do pai
        super().__init__(name=name, design=design, description=description, area_of_effect=area_of_effect)

        # Dano do equipamento
        self.damage = damage

    def __str__(self):
        return self.name