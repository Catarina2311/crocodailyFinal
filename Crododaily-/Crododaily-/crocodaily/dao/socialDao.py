from dao.conexao import Conexao
from model.socialModel import SocialModel

class SocialDao:

    def insert(self, social):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO social (avaliacao)
            VALUES (%s)
        """

        valores = (social.getAvaliacao(),)

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM social"

        cursor.execute(sql)

        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return dados
    
    
    def update(self, social):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE social
            SET avaliacao = %s
            WHERE idSocial = %s
        """

        valores = (
            social.getAvaliacao(),
            social.getIdSocial()
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()

    def delete(self, idSocial):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM social WHERE idSocial = %s"

        cursor.execute(sql, (idSocial,))

        conexao.commit()

        cursor.close()
        conexao.close()