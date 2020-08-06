# Funções para gerenciar os arquivos do meu sistema
import os
import pickle


"""
    @Parametro:
        * arqWay: Caminho do arquivo
    @Acoes: 
        1- cria arquivo no caminho especificado 
"""
def create_file(arqWay):

    try:
        with open(arqWay, 'wb') as file:
            pickle.dump({}, file, pickle.HIGHEST_PROTOCOL)
    except FileNotFoundError as e1:
        raise e1
    except Exception as e2:
        raise e2

"""
    @Parametro:
        * arqWay: Caminho do arquivo
    @Acoes: 
        1- verifica se o arquivo existe
"""
def file_exists(arqWay):
    return os.path.isfile(arqWay)