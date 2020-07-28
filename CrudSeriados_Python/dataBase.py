#salvar em modo binario
import os
import pickle 



class DataBase:

    #pegar caminho atual e juntar com 'series.pkl'
    arqWay = os.path.join(os.getcwd(),'series.pkl')

    def __init__(self):
        self.dados = {}

    #Salvar dados em arquivo binario
    def dataSave(self):
        try:
            with open (self.arqWay, 'wb') as file:
                pickle.dump(self.dados,file,pickle.HIGHEST_PROTOCOL)
            print("Salvo com sucesso")
            return True
        except Exception as e:
            print('Erro ao salvar dados')
            print(str(e))
            return False
    
    #Carregar arquivo em modo binario
    def loadData(self):
        with open(self.arqWay, 'rb') as file:
            try:
                self.dados = pickle.load(file)
                return True
            except EOFError as e:
                print(str(e))
                return False

    #Mostrar os dados
    def showAll(self):
        if not self.dados:
            print("Não ha dados")
        else:
            for nome, serie in self.dados.items():
                print(f'{nome}: {serie}')

    #Buscar series em O(1)
    def searchSerie(self,serieName):
        return self.dados.get(serieName)
