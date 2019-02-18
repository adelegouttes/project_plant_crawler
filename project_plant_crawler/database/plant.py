from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


plants_harvest_months_association = Table(
    'plants_harvest_months',  Base.metadata,
    Column('plant_id', String, ForeignKey('plants.plant_id')),
    Column('harvest_month_id', Integer, ForeignKey('months.month_id'))
)


class Plant(Base):
    __tablename__ = 'plants'
    plant_id = Column(String(50), unique=True, primary_key=True)
    name = Column(String(150), unique=False)
    family = Column(String(150), unique=False)
    harvest_months = relationship("Month", secondary=plants_harvest_months_association)

    def __init__(self, plant_id=None, name=None, family=None):
        self.name = name
        self.plant_id = plant_id
        self.family = family

    def __repr__(self):
        return '<Plant %r>' % (self.name)

