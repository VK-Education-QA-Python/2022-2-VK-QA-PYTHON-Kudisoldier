import requests
from dataclasses import dataclass


@dataclass
class ApiResponse:
    """Class for handling request data."""
    json: dict or None
    text: str
    status_code: int
    url: str


class BaseApi:
    def __init__(self):
        self.base_url = 'https://target-sandbox.my.com/'
        self.session = requests.Session()

    def _request(self, method: str, url: str, **kwargs) -> ApiResponse:
        requests_response = self.session.request(method, url, **kwargs)

        try:
            response_json = requests_response.json()
        except requests.JSONDecodeError:
            response_json = None

        return ApiResponse(json=response_json, status_code=requests_response.status_code,
                           url=requests_response.url, text=requests_response.text)

    def get_cookies(self, method: str, url: str) -> dict:
        requests_response = self.session.request(method, url)
        return requests_response.cookies.get_dict()

