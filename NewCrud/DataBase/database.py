import os
import pickle
import sys

from NewCrud.gerencia_de_arquivos import file_manager
from NewCrud.tratamento_de_erros import exception_messages
from NewCrud.tratamento_de_erros.my_exception import MyException
from NewCrud.player import Player

class DataBase:
    arqWay = os.path.join(os.getcwd(), 'players.pkl')

    def __init__ (self):
        self.players = {}
        self.dataLoad()
    """
        @Parametro:
            * gamertag: nome do jogador
            * password: senha do jogador
        @Acoes: Criar novo usuario e salva-lo no banco de dados
    """    
    def create(self, gamertag, password):
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)
        if self.player_exists(gamertag):
            raise MyException(exception_messages.PLAYER_ALREADY_REGISTERED)    
        player = Player(gamertag,password, 0, None, [])
        self.players[gamertag] = player
        self.dataSave()


    """
        @Parametro:
            * gamertag: nome do jogador
            * password: senha do jogador
        @Acoes: Ler usuario e retorna-lo
    """
    def read(self, gamertag, password):
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)
        if not self.player_exists(gamertag):
            raise MyException(exception_messages.PLAYER_NOT_FOUND)

        player = self.players.get(gamertag)        
        if player.password != password:
            raise MyException(exception_messages.WRONG_PASSWORD)
        return player


    """
        @Parametro:
            * gamertag: nome do jogador
            * password: senha do jogador
            * new_gamertag: novo nome de jogador
        @Acoes: 
            1- buscar jogador na tabela
            2- excluir jogador da tabela hash
            3- atualizar a gamertag
            4- salvar os dados ja atualizados
    """
    def update_gamertag(self, gamertag, password, new_gamertag):
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)
       
        if not new_gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)
       
        try:
            # Buscando jogador na tabela Hash
            player = self.read(gamertag, password)
            del self.players[gamertag]

            # Atualizando a gamertag do jogador
            player.gamertag = new_gamertag

            self.players[new_gamertag] = player
            self.dataSave()
            return True
        except MyException as e:
            raise e


    """
        @Parametro:
            * gamertag: nome do jogador
            * password: senha do jogador
            * new_password: novo nome de jogador
        @Acoes: 
            1- buscar jogador na tabela
            2- excluir jogador da tabela hash
            3- atualizar a senha
            4- salvar os dados ja atualizados
    """
    def update_password(self, gamertag, password, new_password):
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)
       
        if not new_password.strip():
            raise MyException(exception_messages.INVALID_PASSWORD)
       
        try:
            # Buscando jogador na tabela Hash
            player = self.read(gamertag, password)
            del self.players[gamertag]

            # Atualizando a gamertag do jogador
            player.password = new_password
            self.dataSave()
            return True
        except MyException as e:
            raise e

    
    """
        @Parametro:
            * gamertag: nome do jogador
            * password: senha do jogador
        @Acoes: 
            1- buscar jogador na tabela
            2- excluir jogador da tabela hash
    """
    def delete(self, gamertag, password):
        try:
            # Buscar jogador na tabela
            player = self.read(gamertag, password)

            del self.players[gamertag]
            del player

            self.dataSave()
            return True
        except MyException as e:
            raise e

    """
        @Acoes: 
            1- testar se banco de dados esta vazio
            2- printar jogadores
    """
    def showAll(self):
        if not self.players:
            print(exception_messages.EMPTY_DATABASE)
        else:
            print('-='*50)
            for player in self.players.values():
                print (player)
                print('-='*50)


    """
        @Acoes: Salvar Dados da RAM para o HD
            1- Abrir arquivo
            2- Adicionar dados
        @Return: boolean 
    """
    def dataSave(self):
        try:
            # Abrindo o arquivo em forma de escrita binaria 
            with open(self.arqWay, 'wb') as file:
                pickle.dump(self.players, file, pickle.HIGHEST_PROTOCOL)
            print('Dados salvos com sucesso!')
            return True
        except Exception as e:
            print('Erro ao salvar os dados')
            print(str(e))
            return False


    """
        @Acoes: Carregar dados do HD para a memoria RA<
            1- Testar se existe o arquivo, caso nao exista, criar
            2- Abrir o arquivo em modo de leitura binaria
        @Return: boolean
    """
    def dataLoad(self):
        if not file_exists(self.arqWay):
            create_file(self.arqWay)
            
        with open(self.arqWay, 'rb') as file:
            try:
                self.players = pickle.load(file)
                return True
            except EOFError as e:
                print(str(e))
                return False


    def player_exists(self, gamertag):
        return False if not self.players or self.players.get(gamertag) is None else True





def file_exists(filepath):
    return os.path.isfile(filepath)

def create_file(arqWay):
    with open(arqWay, 'wb') as file:
        pickle.dump({}, file, pickle.HIGHEST_PROTOCOL)

    