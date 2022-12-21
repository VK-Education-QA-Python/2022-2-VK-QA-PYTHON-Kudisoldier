import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.users_model import UserModel


class DatabaseClient:
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self):
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def truncate_table(self, table_name):
        self.execute_query(f'TRUNCATE TABLE {self.db_name}.{table_name};')

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def add_user(self, name, surname, middle_name, username, password, email, access, active, start_active_time):
        self.session.add(UserModel(name, surname, middle_name, username,
                                   password, email, access, active, start_active_time))
        self.session.commit()

    def get_user(self, username):
        self.session.commit()
        return self.session.query(UserModel).where(UserModel.username == username).all()

    def block_user(self, username):
        current_user = self.session.execute(sqlalchemy.select(UserModel).filter_by(username=username)).scalar_one()
        current_user.access = 0
        self.session.commit()
