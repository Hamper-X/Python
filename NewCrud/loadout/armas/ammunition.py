class Ammunition:
    
    """
        @Paramero: 
            * bullets: Quantidade de balas que o jogador tera disponivel.
            * type: Calibre da munição do jogador (7.62, 5.56, 9mm, .45, .50BMG...)
    """
    def __init__(self, bullets, type):
        
        self.bullets = bullets
        self.type = type