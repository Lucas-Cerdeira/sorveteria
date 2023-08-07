from sqlalchemy.orm import DeclarativeBase



class ModelBase(DeclarativeBase):
    pass
    __allow_unmapped__ = True
