from dao.conexao import Conexao
from model.inicialModel import InicialModel

class InicialDao:

    def insert(self, inicial):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO inicial (descricao)
            VALUES (%s)
        """

        valores = (inicial.getDescricao(),)

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM inicial"

        cursor.execute(sql)

        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return dados

    def update(self, inicial):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE inicial
            SET descricao = %s
            WHERE idInicial = %s
        """

        valores = (
            inicial.getDescricao(),
            inicial.getIdInicial()
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()

    def delete(self, idInicial):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM inicial WHERE idInicial = %s"

        cursor.execute(sql, (idInicial,))

        conexao.commit()

        cursor.close()
        conexao.close()