from sqlalchemy import Column, Text, String
from database import Base


class Plant(Base):
    __tablename__ = 'plants'
    code = Column(String(50), unique=True, primary_key=True)
    name = Column(String(150), unique=False)
    family = Column(String(150), unique=False)
    description_raw = Column(Text, unique=False)

    def __init__(self, code=None, name=None, family=None, description_raw=None):
        self.name = name
        self.code = code
        self.family = family
        self.description_raw = description_raw

    def __repr__(self):
        return '<Plant %r>' % (self.name)