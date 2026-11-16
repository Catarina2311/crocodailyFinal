class InicialModel:

    def __init__(self, idInicial, descricao):
        self.__idInicial = idInicial
        self.__descricao = descricao

    def getIdInicial(self):
        return self.__idInicial

    def setIdInicial(self, idInicial):
        self.__idInicial = idInicial

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao