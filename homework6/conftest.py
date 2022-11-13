import pytest
from database_client import DatabaseClient
from models.count_requests import CountRequestsModel
from models.requests_type_count import RequestsTypeModel
from models.top_frequent_requests import TopFrequentModel
from models.top_biggest_requests import TopBiggestModel
from models.top_requests_failed import TopFailedModel


def pytest_configure(config):
    database_client = DatabaseClient('127.0.0.1', '3306', 'root', 'pass', 'TEST_SQL')
    if not hasattr(config, 'workerinput'):
        database_client.create_db()
    database_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        database_client.create_table(CountRequestsModel.__tablename__)
        database_client.create_table(RequestsTypeModel.__tablename__)
        database_client.create_table(TopFrequentModel.__tablename__)
        database_client.create_table(TopBiggestModel.__tablename__)
        database_client.create_table(TopFailedModel.__tablename__)

    config.database_client = database_client


@pytest.fixture(scope='session')
def database_client(request):
    database_client = request.config.database_client
    yield database_client
    database_client.connection.close()
