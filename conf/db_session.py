from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_base import ModelBase



engine = create_engine('mysql+pymysql://root:root@localhost:3306/picoles')


Session = sessionmaker(engine)
session = Session()


def create_tables():
    
    import models.__all_models
    ModelBase.metadata.drop_all(engine)
    ModelBase.metadata.create_all(engine)
    