from sqlalchemy import Column, Integer, VARCHAR
from models.base_model import Base


class TopBiggestModel(Base):
    __tablename__ = 'top_biggest_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.url} {self.status_code} {self.size} {self.ip}'

    def __init__(self, url, status_code, size, ip):
        self.url = url
        self.status_code = status_code
        self.size = size
        self.ip = ip

    url = Column(VARCHAR(312), nullable=False, primary_key=True)
    status_code = Column(Integer)
    size = Column(Integer)
    ip = Column(VARCHAR(312), nullable=False)
