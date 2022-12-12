from sqlalchemy import Column, VARCHAR, INT, SMALLINT, DATETIME
from models.base_model import Base


class UserModel(Base):
    __tablename__ = 'test_users'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'{self.username} {self.name} {self.active}'

    def __init__(self, name, surname, middle_name, username, password, email, access, active, start_active_time):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.username = username
        self.password = password
        self.email = email
        self.access = access
        self.active = active
        self.start_active_time = start_active_time

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR)
    surname = Column(VARCHAR)
    middle_name = Column(VARCHAR)
    username = Column(VARCHAR)
    password = Column(VARCHAR)
    email = Column(VARCHAR)
    access = Column(SMALLINT)
    active = Column(SMALLINT)
    start_active_time = Column(DATETIME)
