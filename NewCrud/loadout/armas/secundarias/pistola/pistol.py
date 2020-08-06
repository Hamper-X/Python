from NewCrud.loadout.armas.secundarias.handgun import Handgun


class Pistol(Handgun):
    def __init__(
            self, name, accuracy, damage, reload_speed, ammunition,
            muzzle, barrel,  laser, optic, dual):

        # Chamando o construtor do pai (Handgun)
        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition, muzzle=muzzle,
            barrel=barrel, laser=laser, optic=optic, dual=dual)