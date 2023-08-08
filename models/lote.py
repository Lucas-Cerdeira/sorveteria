import sqlalchemy as sa
from sqlalchemy.orm import relationship
from datetime import datetime
from models.tipo_picole import TipoPicole
from models.model_base import ModelBase


class Lote(ModelBase):
    __tablename__ = 'lotes'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_Criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'))
    tipo_picole = relationship('TipoPicole', lazy='joined')
    
    quantidade: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'
   