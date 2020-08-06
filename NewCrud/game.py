from NewCrud.menus.main_menu import MainMenu
from NewCrud.tratamento_de_erros import exception_messages
from NewCrud.dados.database import Database
from NewCrud.tratamento_de_erros.my_exception import MyException
class Game:
    def __init__(self):
        self.database = DataBase()
        self.online_players = []

    """
        @Parametros: Entradas dos usuarios
    """
    def createPlayerAccount(self, gamertag, password):
        try:    
            self.database.create(gamertag, password)
            print("Sua conta foi criada com sucesso!")  
        except MyException as e:
            print(str(e))

    """
        @Parametros: Entradas do usuario
            * gamertag: nome do jogador
            * password: senha do jogador
        @Acoes: Dados do usuario farão login no jogo
    """
    def login(self, gamertag, password):
        try: 
            player = self.database.read(gamertag, password)
            print(f'Seja bem vindo, {player.gamertag}!')
            self.online_players.append(player)
            return player
        except MyException as e:
            if str(e) == exception_messages.EMPTY_DATABASE:
                print('Jogador não cadastrado!')
            else:
                print(str(e))


    """
        @Parametro: Dados do input do usuario
            * gamertag: nome do jogador
            * password: senha do jogador
            * new_password: nova senha escolhida pelo jogador
        @Acoes: Realizar a troca da senha
    """
    def updatePlayerPassword(self, gamertag, password, new_password):
        try:
            self.database.update_password(gamertag, password, new_password)
            print(f'Senha atualizada com sucesso!')
        except MyException as e:
            print(e)


    """
        @Parametro: Dados do inputs do usuario
            * gamertag: nome do jogador
            * password: senha do jogador
            * new_gamertag: nova gamertag escolhida pelo jogador

        @Acoes: Altera a gamertag do jogador
    """
    def updatePlayerGamertag(self, gamertag, password, new_gamertag):
        try:
            self.database.update_gamertag(gamertag, password, new_gamertag)
            print(f'Gamertag atualizada com sucesso!')
        except MyException as e:
            print(e)


    """
        @Parametro: Dados dos inputs do usuario
            * gamertag: nome do jogador
            * password: senha do jogador
        @Acoes: Remove a conta do jogador
    """
    def deletePlayerAccount(self, gamertag, password):
        try:
            self.database.delete(gamertag, password)
            print(f'Conta removida com sucesso!')
        except MyException as e:
            print(e)

    
        