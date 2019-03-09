from sqlalchemy import Column, String, Integer
from project_plant_crawler.database.base import Base


class Month(Base):
    __tablename__ = 'months'
    month_id = Column(Integer, unique=True, primary_key=True)
    month_name_eng = Column(String(50), unique=True)

    def __init__(self, month_id=1, month_name_eng='January'):
        self.month_id = month_id
        self.month_name_eng = month_name_eng

    def __repr__(self):
        return '<Month %r>' % self.month_name_eng

    def to_dict(self):
        return {'id': self.month_id, 'name': self.month_name_eng}

