from sqlalchemy import Column, Integer, VARCHAR
from models.base_model import Base


class TopFailedModel(Base):
    __tablename__ = 'top_user_requests_failed'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.ip} {self.failed_count}'

    def __init__(self, ip, failed_count):
        self.ip = ip
        self.failed_count = failed_count

    ip = Column(VARCHAR(312), nullable=False, primary_key=True)
    failed_count = Column(Integer)
