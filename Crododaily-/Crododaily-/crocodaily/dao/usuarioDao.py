
from dao.conexao import Conexao

class UsuarioDao:

    def buscar_por_usuario(self, usuario):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT * FROM usuarios
            WHERE usuario = %s
        """

        cursor.execute(sql, (usuario,))
        dados = cursor.fetchone()

        cursor.close()
        conexao.close()

        return dados

    def inserir(self, usuario, senha):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO usuarios (usuario, senha)
            VALUES (%s, %s)
        """

        cursor.execute(sql, (usuario, senha))

        conexao.commit()

        cursor.close()
        conexao.close()
