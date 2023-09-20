from sqlalchemy import create_engine, MetaData, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


engine = create_engine('')
meta_data = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base(metadata=meta_data, bind=engine)
Base.query = db_session.query_property()


class PrimaryKeyIdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class Fleetmanager(Base, PrimaryKeyIdMixin):
    __tablename__ = 'fleetmanagers'
    fleetmanager_id = Column(String(255))
    fleet_id = Column(JSONB)
    actions = Column(JSONB)
 

class Datasubmanager(Base, PrimaryKeyIdMixin):
    __tablename__ = 'datasubmanagers'
    datasubmanager_id = Column(String(255))
    fleet_id = Column(String(255))
    actions = Column(JSONB)
    
if __name__ == '__main__':
    meta_data.create_all()
