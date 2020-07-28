
from serie import Serie
from dataBase import DataBase

# FUNÇÕES ============================================================================================================

"""
    Parametro: caminho para o arquivo HTML
    Objetivo Funcao: filtrar as tags
    Retorno: Lista de objetos 'Serie'
    Acoes:
        - Abrir arquivo html modo leitura 
        - Retirar tags desnecessarias
        - Separar apenas nome,ano e avaliação
"""

def get_seriesList(arqWay_html):

    with open (arqWay_html, 'r') as file:
        titleTag = '<td class="titleColumn">'
        serieList = []

        while True:
            linha = file.readline()
            if not linha:
                break
            if titleTag in linha:
                _ = file.readline() #descarte de linha

                #get serie name 
                linha = file.readline()
                nome = clearTag(linha) 
                 
                #get serie year
                linha = file.readline()
                ano = clearTag(linha)

                #jump 2 lines
                _ = file.readline()
                _ = file.readline()

                #get serie avaliation
                linha = file.readline()
                avaliacao = clearTag(linha)

                newSerie = Serie(nome, ano, avaliacao)
                serieList.append(newSerie)

        return serieList


"""
    Parametro: lista de objetos
    Objetivo Funcao: criação a alocação de valores em hash, buscando a complexidade O(1)
    Retorno: tabela hash em modo dicionario
"""
def creatHash(serieList):
    hashTable = {}
    for serie in serieList:
        nome = serie.nome
        hashTable[nome] = serie
    return hashTable



"""
    Parametro: linha do html(string) 
    Objetivo Funcao: limpeza das tags e seleção dos dados
    Retorno: Substring com valores
"""
def clearTag(linha):
    inicio = linha.find('>')
    fim = linha.rfind('<')
    return linha[inicio+1:fim]


# MAIN ============================================================================================================
def main():
    
    dataBase = DataBase()
    #inicialização
    """way = "A:\Dados Gerais\David\Minha Carreira\Projetos\crud_pyEscolaFerias\series.html"
    serieList = get_seriesList(way)
    hashTable = creatHash(serieList)
    dataBase.dados = hashTable
    dataBase.dataSave()"""
    anser = dataBase.loadData()
    if anser:
        userCall = input("Qual serie deseja pesquisar?")
        serie = dataBase.searchSerie(userCall)

        if serie is not None:
            print(serie)
        else:
            print(f'a serie {userCall} não esta cadastrada na rede')

if __name__ == '__main__':
    main()

