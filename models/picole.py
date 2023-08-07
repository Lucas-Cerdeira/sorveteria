import sqlalchemy as sa
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List, Optional
from models.model_base import ModelBase
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.sabor import Sabor
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo


ingredientes_picole = sa.Table('ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id')),
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
    )

conservantes_picole = sa.Table(
    'conservante_picole',
    ModelBase.metadata,
    sa.Column('id_conservantes', sa.Integer,sa.ForeignKey('conservantes.id')),
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')) 
)

aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id')),
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
    )

class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    data_Criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Sabor = relationship('Sabor', lazy='joined') 

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = relationship('TipoEmbalagem', lazy='joined')
    
    id_tipo_Picole: int = sa.Column(sa.Integer, sa.ForeignKey('picoles.id'))
    tipo_picole: TipoPicole = relationship('TipoPicole', lazy='joined')

    ingredientes: List[Ingrediente] = relationship('Lote', secondary=ingredientes_picole, backref='ingredientes', lazy='dynamic')
    conservantes: Optional[List[Conservante]] = relationship('Conservante', secondary=conservantes_picole, backref='conservantes', lazy='dynamic')
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = relationship('AditivoNutrivo', secondary=aditivos_nutritivos_picole, backref='aditivos_nutritivos', lazy='dynamic')

    def __repr__(self) -> str:
        return f'<Sabor: {self.sabor.nome}> <Preço: {self.preco}'