import sqlalchemy as sa
from models.model_base import ModelBase


class TipoEmbalagem(ModelBase):
    __tablename__ = 'tipos_embalagem'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(45))

    def __repr__(self) -> str:
        return f'<Tipo Embalagem: {self.nome}>'