class GeralModel:

    def __init__(self, idGeral, descricao):
        self.__idGeral = idGeral
        self.__descricao = descricao

    def getIdGeral(self):
        return self.__idGeral

    def setIdGeral(self, idGeral):
        self.__idGeral = idGeral

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao