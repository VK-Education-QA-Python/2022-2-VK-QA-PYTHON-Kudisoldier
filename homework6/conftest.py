import pytest
from database_client import DatabaseClient
from models.count_requests import CountRequestsModel
from models.requests_type_count import RequestsTypeModel
from models.top_frequent_requests import TopFrequentModel
from models.top_biggest_requests import TopBiggestModel
from models.top_requests_failed import TopFailedModel
import os


@pytest.fixture()
def repo_root():
    return os.path.abspath(os.getcwd())


def pytest_configure(config):
    database_client = DatabaseClient('127.0.0.1', '3306', 'root', 'pass', 'TEST_SQL')
    if not hasattr(config, 'workerinput'):
        database_client.create_db()
    database_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        tables = [CountRequestsModel.__tablename__, RequestsTypeModel.__tablename__,
                  TopFrequentModel.__tablename__, TopBiggestModel.__tablename__,
                  TopFailedModel.__tablename__]
        for table in tables:
            database_client.create_table(table)

    config.database_client = database_client


@pytest.fixture(scope='session')
def database_client(request):
    database_client = request.config.database_client
    yield database_client
    database_client.connection.close()
