from sqlalchemy import Column, Integer, VARCHAR
from models.base_model import Base


class RequestsTypeModel(Base):
    __tablename__ = 'requests_type_count'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.requests_type} {self.requests_type_count}'

    def __init__(self, requests_type, requests_type_count):
        self.requests_type_count = requests_type_count
        self.requests_type = requests_type

    requests_type = Column(VARCHAR(312), nullable=False, primary_key=True)
    requests_type_count = Column(Integer)
