from NewCrud.loadout.armas.weapon import Weapon


# Classe "Assault Rifle", tem como herança a classe "Weapon"
class AssaultRifle(Weapon):
    
    """ 
        Construtor da classe 'Assault Rifle'
            - Usando classe construtora do pai (Weapon)
            - Inicialização de atributos especificos da classe AssaultRifle
    """
    def __init__(self, name, accuracy, damage, muzzle, barrel, laser,
                 optic, ammunition, reload_speed, stock, underbarrel ):
        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic)
        self.stock = stock
        self.underbarrel = underbarrel

    """
    Usando polimorfismo de sobreposição para sobrescrever o metodo shoot() da classe pai (override)
    """
    def shoot(self):
        print("Atirando com assault rifle")
    
    """
    Usando polimorfismo de sobreposição para sobrescrever o metodo reload() da classe pai (override)
    """
    def reload(self):
        print("Recarregando Assalt Rifle")
    
                