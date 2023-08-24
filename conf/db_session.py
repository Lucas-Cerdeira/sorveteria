from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.model_base import ModelBase



engine = create_engine('mysql+pymysql://root:root@localhost:3306/picoles')

def create_session():
    __session = sessionmaker(engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session




def create_tables():
    
    import models.__all_models
    ModelBase.metadata.drop_all(engine)
    ModelBase.metadata.create_all(engine)
    