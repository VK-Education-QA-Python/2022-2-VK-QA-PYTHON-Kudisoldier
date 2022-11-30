from models.count_requests import CountRequestsModel
from models.requests_type_count import RequestsTypeModel
from models.top_frequent_requests import TopFrequentModel
from models.top_biggest_requests import TopBiggestModel
from models.top_requests_failed import TopFailedModel
import re


class DataBuilder:
    def __init__(self, client):
        self.client = client

    def requests_count(self, repo_root):
        with open(repo_root + '/homework6/nginx_log.txt') as file:
            requests_count = len(file.readlines())
        self.client.session.add(CountRequestsModel(requests_count))

    def requests_type(self, repo_root):
        d = {}
        with open(repo_root + '/homework6/nginx_log.txt') as file:
            for i in file:
                method = i.split(' ')[5][1:]

                if d.get(method) is not None:
                    d[method] += 1
                else:
                    d[method] = 1

        for item in sorted(d.items(), key=lambda a: int(a[1])):
            self.client.session.add(RequestsTypeModel(item[0], int(item[1])))

    def requests_top_count(self, repo_root):
        d = {}
        with open(repo_root + '/homework6/nginx_log.txt') as file:
            for i in file:
                path = i.split(' ')[6]
                location = re.search(r'(?<!:)(?<!\/)\/[^?]*', path)[0]

                if d.get(location) is not None:
                    d[location] += 1
                else:
                    d[location] = 1

        d = dict(sorted(d.items(), key=lambda a: int(a[1]))[-10:])

        for item in d.items():
            self.client.session.add(TopFrequentModel(item[0], int(item[1])))

    def requests_top_biggest(self, repo_root):
        requests = []
        with open(repo_root + '/homework6/nginx_log.txt') as file:
            for i in file:
                request = i.split(' ')
                if re.match(r'4\d\d', request[8]):
                    requests.append([request[0], request[6], request[8], request[9]])

        requests = sorted(requests, key=lambda a: int(a[3]))[-5:]

        for item in requests:
            self.client.session.add(TopBiggestModel(item[1], int(item[2]), int(item[3]), item[0]))

    def requests_top_failed(self, repo_root):
        d = {}
        with open(repo_root + '/homework6/nginx_log.txt') as file:
            for i in file:
                request = i.split(' ')
                if re.match(r'5\d\d', request[8]):
                    if d.get(request[0]) is not None:
                        d[request[0]] += 1
                    else:
                        d[request[0]] = 1

        d = dict(sorted(d.items(), key=lambda a: int(a[1]))[-5:])

        for item in d.items():
            self.client.session.add(TopFailedModel(item[0], int(item[1])))
