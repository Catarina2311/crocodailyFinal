from dao.conexao import Conexao
from model.geralModel import GeralModel

class GeralDao:

    def insert(self, geral):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO geral (descricao)
            VALUES (%s)
        """

        valores = (geral.getDescricao(),)

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM geral"

        cursor.execute(sql)

        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return dados

    def update(self, geral):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE geral
            SET descricao = %s
            WHERE idGeral = %s
        """

        valores = (
            geral.getDescricao(),
            geral.getIdGeral()
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()

    def delete(self, idGeral):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM geral WHERE idGeral = %s"

        cursor.execute(sql, (idGeral,))

        conexao.commit()

        cursor.close()
        conexao.close()