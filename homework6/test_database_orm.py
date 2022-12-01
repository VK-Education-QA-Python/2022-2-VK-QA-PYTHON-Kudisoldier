import subprocess
import pytest
from builder import DataBuilder
from models.count_requests import CountRequestsModel
from models.requests_type_count import RequestsTypeModel
from models.top_frequent_requests import TopFrequentModel
from models.top_biggest_requests import TopBiggestModel
from models.top_requests_failed import TopFailedModel


class SqlTestBase:
    def prepare(self, repo_root):
        raise NotImplemented

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, database_client, repo_root):
        self.database_client = database_client
        self.builder = DataBuilder(self.database_client)
        self.prepare(repo_root)


class TestRequestsCount(SqlTestBase):
    def get_requests_count(self):
        self.database_client.session.commit()
        return self.database_client.session.query(CountRequestsModel).all()

    def prepare(self, repo_root):
        self.builder.requests_count(repo_root)

    def test_requests_count(self, repo_root):
        requests_count = self.get_requests_count()
        bash_res = subprocess.check_output(repo_root + '/homework6/scripts/count_requests.bash '
                                           + repo_root + '/homework6/nginx_log.txt', shell=True).decode('utf-8')
        assert str(requests_count[0]) == bash_res[:-1]


class TestRequestsTypeCount(SqlTestBase):
    def get_requests_type_count(self):
        self.database_client.session.commit()
        return self.database_client.session.query(RequestsTypeModel). \
            order_by(RequestsTypeModel.requests_type_count).all()

    def prepare(self, repo_root):
        self.builder.requests_type(repo_root)

    def test_requests_count(self, repo_root):
        requests_type_count = self.get_requests_type_count()

        bash_res = subprocess.check_output(repo_root + '/homework6/scripts/count_requests_type.bash '
                                           + repo_root + '/homework6/nginx_log.txt', shell=True).decode('utf-8')

        assert [repr(requests_type_count[i]) for i in range(len(requests_type_count))] == bash_res.splitlines()


class TestTopFrequent(SqlTestBase):
    def get_requests_top_count(self):
        self.database_client.session.commit()
        return self.database_client.session.query(TopFrequentModel). \
            order_by(TopFrequentModel.requests_count).all()

    def prepare(self, repo_root):
        self.builder.requests_top_count(repo_root)

    def test_top_frequent_requests(self, repo_root):
        requests_count = self.get_requests_top_count()

        bash_res = subprocess.check_output(repo_root + '/homework6/scripts/top_frequent_requests.bash '
                                           + repo_root + '/homework6/nginx_log.txt', shell=True).decode('utf-8')
        db_res = [repr(requests_count[i]).split() for i in range(len(requests_count))]
        flatten_list = [j for sub in db_res for j in sub]
        assert len(flatten_list) == len(bash_res.splitlines())


class TestTopBiggest(SqlTestBase):
    def get_biggest_requests(self):
        self.database_client.session.commit()
        return self.database_client.session.query(TopBiggestModel).all()

    def prepare(self, repo_root):
        self.builder.requests_top_biggest(repo_root)

    def test_top_biggest_requests(self, repo_root):
        requests_top_biggest = self.get_biggest_requests()
        db_res = [repr(requests_top_biggest[i]).split() for i in range(len(requests_top_biggest))]
        flatten_list = [j for sub in db_res for j in sub]
        bash_res = subprocess.check_output(repo_root + '/homework6/scripts/top_biggest_requests.bash '
                                           + repo_root + '/homework6/nginx_log.txt', shell=True).decode('utf-8')

        assert len(flatten_list) == len(bash_res.splitlines())


class TestTopFailed(SqlTestBase):
    def get_top_failed_requests(self):
        self.database_client.session.commit()
        return self.database_client.session.query(TopFailedModel).order_by(TopFailedModel.failed_count).all()

    def prepare(self, repo_root):
        self.builder.requests_top_failed(repo_root)

    def test_top_biggest_requests(self, repo_root):
        requests_top_failed = self.get_top_failed_requests()
        db_res = [repr(requests_top_failed[i]).split() for i in range(len(requests_top_failed))]
        flatten_list = [j for sub in db_res for j in sub]
        bash_res = subprocess.check_output(repo_root + '/homework6/scripts/top_user_requests_failed.bash '
                                           + repo_root + '/homework6/nginx_log.txt', shell=True).decode('utf-8')

        assert flatten_list == bash_res.splitlines()

