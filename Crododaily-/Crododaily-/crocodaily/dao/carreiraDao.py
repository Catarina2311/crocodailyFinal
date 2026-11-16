from dao.conexao import Conexao
from model.carreiraModel import CarreiraModel

class CarreiraDao:

    def insert(self, carreira):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO carreira (avaliacao)
            VALUES (%s)
        """

        valores = (carreira.getAvaliacao(),)

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM carreira"

        cursor.execute(sql)

        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return dados
    
    
    def update(self, carreira):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE carreira
            SET avaliacao = %s
            WHERE idCarreira = %s
        """

        valores = (
            carreira.getAvaliacao(),
            carreira.getIdCarreira()
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()

    def delete(self, idCarreira):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM carreira WHERE idCarreira = %s"

        cursor.execute(sql, (idCarreira,))

        conexao.commit()

        cursor.close()
        conexao.close()