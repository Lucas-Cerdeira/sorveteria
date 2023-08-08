import sqlalchemy as sa
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List
from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote


#Uma nota fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.BigInteger, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', sa.BigInteger, sa.ForeignKey('lotes.id'))
)



class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)

    numero_serie: str = sa.Column(sa.String(45),unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)

    id_revendedor: Revendedor = sa.Column(sa.BigInteger, sa.ForeignKey('revendedores.id'))
    revendedor: Revendedor = relationship('Revendedor', lazy='joined')

    #Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f'<Sabor: {self.numero_serie}>'