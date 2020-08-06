from NewCrud.loadout.armas.weapon import Weapon


class Handgun(Weapon):
    def __init__(
            self, name, accuracy, damage, reload_speed,
            ammunition, muzzle, barrel, laser, optic, dual):

        # Chamando o construtor do pai
        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic)

        self.dual = dual