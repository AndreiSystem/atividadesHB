from dao.base_dao import BaseDao
from model.cotacao_diaria import CotacaoDiaria

class CotacaoDiariaDao(BaseDao):
    def __init__(self):
        self.model = CotacaoDiaria
        super().__init__(self.model)

    
    def listar_cotacao(self):
        #dados = self.session.query(self.model).all()
        dados = self.list_all()

        for p in dados:
            p.pl = p.valor_fechamento / p.lpa


        return sorted(dados, key= CotacaoDiaria.get_pl)

        
        