from sqlalchemy import Column, String, Integer
from base import Base


class Month(Base):
    __tablename__ = 'plants'
    id = Column(Integer, unique=True, primary_key=True)
    name_fr = Column(String(50), unique=True)
    name_eng = Column(String(50), unique=True)

    def __init__(self, id=1, name_fr='Janvier', name_eng='January'):
        self.id = id
        self.name_fr = name_fr
        self.name_eng = name_eng

    def __repr__(self):
        return '<Month %r>' % self.name_eng

