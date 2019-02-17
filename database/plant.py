from sqlalchemy import Column, Text, String
from base import Base


class Plant(Base):
    __tablename__ = 'plants'
    code = Column(String(50), unique=True, primary_key=True)
    name = Column(String(150), unique=False)
    family = Column(String(150), unique=False)

    def __init__(self, code=None, name=None, family=None, description_raw=None):
        self.name = name
        self.code = code
        self.family = family

    def __repr__(self):
        return '<Plant %r>' % (self.name)
