import requests
from dataclasses import dataclass
import logging


@dataclass
class ApiResponse:
    """Class for handling request data."""
    json: dict or None
    text: str
    status_code: int
    url: str


class BaseApi:
    def __init__(self):
        self.base_url = None
        self.logging = False
        self.session = requests.Session()

    def _request(self, method: str, url: str, **kwargs) -> ApiResponse:
        requests_response = self.session.request(method, self.base_url + url, **kwargs)

        try:
            response_json = requests_response.json()
        except requests.JSONDecodeError:
            response_json = None

        if self.logging is True:
            log = logging.getLogger(__name__)
            log.debug(f'{requests_response.status_code} {requests_response.headers} {requests_response.json()}')

        return ApiResponse(json=response_json, status_code=requests_response.status_code,
                           url=requests_response.url, text=requests_response.text)
