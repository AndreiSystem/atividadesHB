import MySQLdb


class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(
            host="mysql.topskills.study", database="topskills05", user="topskills05", passwd="Andrei2019")
        self.cursor = self.conexao.cursor()

    def inserir(self, comando_sql_insert):
        self.cursor.execute(comando_sql_insert)
        self.conexao.commit()