from sqlalchemy import Column, Integer, VARCHAR
from models.base_model import Base


class TopFrequentModel(Base):
    __tablename__ = 'top_frequent_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.path} {self.requests_count}'

    def __init__(self, path, requests_count):
        self.requests_count = requests_count
        self.path = path

    path = Column(VARCHAR(312), nullable=False, primary_key=True)
    requests_count = Column(Integer)
