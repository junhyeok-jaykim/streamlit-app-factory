"""
https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#defining-table-metadata-with-the-orm

When using the ORM, the process by which we declare Table metadata is usually 
combined with the process of declaring mapped classes. 
The mapped class is any Python class we’d like to create, 
which will then have attributes on it that will be linked to the columns
in a database table.
"""
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import (
    registry,
    declarative_base,
    sessionmaker,
    relationship, 
    backref
)
from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html
    Integer, String, Date, DateTime
)

# Connecting database
# NOTE: Remove echo=True in production mode
# future = True for the full use of 2.0 style usage
if __name__ == '__main__':
    # for test
    engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
else:
    engine = create_engine('sqlite+pysqlite:///test.db', echo=True, future=True)

# create session
Session = sessionmaker(bind=engine)

# When using the ORM, the MetaData collection is contained 
# within an ORM-only object known as the `registry`. 
Base = declarative_base()
# mapper_registry = registry()
# Base = mapper_registry.generate_base()


@dataclass
class RunningApp:
    """ 현재 사용중인 앱의 정보들; 요청이 있을 때마다 서버에 조회를 하여 가져온다 """
    pid: int = -1
    port: int  = -1
    hostname: int  = 'unk'
    desc: str = 'unk'
    created_at: str = 'unk'
    runner: str = 'unk'
    # sample: List[str] = field(default_factory=list)
    # sample: List[dict] = field(default_factory=list)


class AppMeta(Base):
    """ Appplication information registered in github repository 

    * path: streamlit app path from the root of git repo
    * desc: app description (should be understandable)
    * runner: submitter name
    """
    __tablename__ = 'app_meta'
    id = Column(String, primary_key=True)
    path = Column(String)
    desc = Column(String)
    runner = Column(String(20))
    made_by = Column(String(20))

    def __repr__(self):
        return "{}({!r})".format(
            self.__class__.__name__,
            {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        )

    @classmethod
    def find_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).all()


class History(Base):
    """ Appplication running history
    """
    __tablename__ = 'history'

    id = Column(ForeignKey('app_meta.id'), primary_key=True, nullable=False)
    created_at = Column(DateTime)
    finished_at = Column(DateTime)
    runner = Column(String)
    status = Column(String)  # success, error, kill
    made_by = Column(ForeignKey('app_meta.made_by'))
    #made_by = Column(String)
    duration = Column(Integer)
    path = Column(ForeignKey('app_meta.path'))
    desc = Column(ForeignKey('app_meta.desc'))
    port = Column(Integer)
    runner = Column(ForeignKey('app_meta.runner'))
    # TODO: log field

    def __repr__(self):
        return "{}({!r})".format(
            self.__class__.__name__,
            {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        )
    
    @classmethod
    def find_all(cls, session):
        return session.query(cls).all()


# create table
Base.metadata.create_all(engine)
# mapper_registry.metadata.create_all(engine)

def test():
    from crud import get_app_meta_from_repo
    session = Session()
    app_meta = get_app_meta_from_repo()
    for x in app_meta:
        print(x)
    temp = History(id=app_meta[0].id, runner=app_meta[0].runner)
    session.add(temp)
    #history = History()
    session.add_all(app_meta)
    session.commit()
    print(f'Current State: {session.new}')
    print(app_meta)


    pass
        
if __name__ == '__main__':
    test()