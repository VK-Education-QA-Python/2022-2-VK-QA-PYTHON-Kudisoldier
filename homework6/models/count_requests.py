from sqlalchemy import Column, Integer
from models.base_model import Base


class CountRequestsModel(Base):
    __tablename__ = 'count_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.requests_count}'

    def __init__(self, requests_count):
        self.requests_count = requests_count

    requests_count = Column(Integer, primary_key=True)
