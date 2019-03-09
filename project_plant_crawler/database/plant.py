from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from project_plant_crawler.database.base import Base


plants_harvest_months_association = Table(
    'plants_harvest_months',  Base.metadata,
    Column('plant_id', String, ForeignKey('plants.plant_id')),
    Column('harvest_month_id', Integer, ForeignKey('months.month_id'))
)
plants_seedling_direct_months_association = Table(
    'plants_seedling_direct_months',  Base.metadata,
    Column('plant_id', String, ForeignKey('plants.plant_id')),
    Column('seedling_direct_month_id', Integer, ForeignKey('months.month_id'))
)
plants_seedling_shelter_months_association = Table(
    'plants_shelter_direct_months',  Base.metadata,
    Column('plant_id', String, ForeignKey('plants.plant_id')),
    Column('seedling_shelter_month_id', Integer, ForeignKey('months.month_id'))
)

class Plant(Base):
    __tablename__ = 'plants'
    plant_id = Column(String(50), unique=True, primary_key=True)
    name = Column(String(150), unique=False)
    family = Column(String(150), unique=False)
    harvest_months = relationship("Month", secondary=plants_harvest_months_association)
    seedling_direct_months = relationship("Month", secondary=plants_seedling_direct_months_association)
    seedling_shelter_months = relationship("Month", secondary=plants_seedling_shelter_months_association)

    def __init__(self, plant_id=None, name=None, family=None):
        self.name = name
        self.plant_id = plant_id
        self.family = family

    def __repr__(self):
        return '<Plant %r>' % (self.name)

    def jsonify(self):
        return {'name': self.name, 'family': self.family, 'plant_id': self.plant_id,
                'harvest_months': [month.to_dict() for month in self.harvest_months],
                'seedling_direct': [month.to_dict() for month in self.seedling_direct_months],
                'seedling_shelter': [month.to_dict() for month in self.seedling_shelter_months]
                }

