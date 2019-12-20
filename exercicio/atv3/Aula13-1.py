

#============= Aula 13 
#=== Data: 18/12/2019
#=== Tema: SqlAlchemy

#===== Instalação do SqlAlchemy
#----- pip3 install sqlalchemy
#----- resultado esperado : Successfully installed sqlalchemy-1.3.12

#===== Instalação do conector Mysql
#----- pip3 install mysql-connector-python
#----- resultado esperado : Successfully installed mysql-connector-python-8.0.18

#===== Usando o SqlAlchemy em projetos
#----- Importação da biblioteca e nomeando-a de acordo com sua preferência
#----- No exemplo abaixo a biblioteca foi nomeada como db mas você pode escolher um nome que faça
#----- mais sentido para você
import sqlalchemy as db

#===== Criando classe para mapeamento de uma tabela do banco de dados
#----- Importação de uma função para gerar a classe base do alchemy e utilizá-la nas classes de modelo
from sqlalchemy.ext.declarative import declarative_base
#----- Definição do nome da classe do alchemy como 'Base'
Base = declarative_base()

#----- Criação de uma classe para representar a tabela da base de dados
class Papel(Base):
#----- Definição do nome da tabela a qual esta classe representa
    __tablename__ = 'PAPEL'

#----- Mapeamento de todas as colunas da tebela
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(length=100))
    tipo_id = db.Column(db.Integer,db.ForeignKey('TIPO.id'),)
    descricao = db.Column(db.String(length=200))
#----- Subscrita do metodo de conversao da classe em string para imprimi-la no terminal
    def __str__(self):
        return f'"id":"{self.id}", "codigo":"{self.codigo}", "tipo_id":{self.tipo_id}, "descricao":"{self.descricao}"'

#===== Criação da engine e Sessao para conexao e consultas na base de dados
#----- Criação da engine informando o conector, usuario, senha, url e a database
engine = db.create_engine('mysql+mysqlconnector://root:170719@localhost:3306/stoks')
#----- Gerando a sessao para realizar as consultas à base de dados
Session = db.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
 
#===== Realizando consultas à base de dados
#----- Listando todos os dados da tabela e exibindo o resultado com um for+print
papeis = session.query(Papel).all()
print(f'\n{5*"="} Todas as linhas da tabela {5*"="}')
for p in papeis:
    print(f'\t{p}')

#----- Listando dados da tabela com limitação de linhas e exibindo o resultado com um for+print
papeis = session.query(Papel).limit(2).all()
print(f'\n{5*"="} Limitando linhas (máximo 2) {5*"="}')
for p in papeis:
    print(f'\t{p}')

#----- Buscando um dado de acordo com uma coluna e exibindo todos os resultados possíveis com um for+print
papeis = session.query(Papel).filter_by(tipo_id=1).all()
print(f'\n{5*"="} Limitando linhas (máximo 2) {5*"="}')
for p in papeis:
    print(f'\t{p}')

#----- Buscando um dado de acordo com uma coluna e exibindo um único resultado com um print
papel = session.query(Papel).filter_by(codigo='BBAS3').first()
print(f'\n{5*"="} Limitando linhas (máximo 2) {5*"="}')
print(f'\t{papel}')
