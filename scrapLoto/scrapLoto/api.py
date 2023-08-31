from dataclasses import dataclass
from scrapLoto.utils import get_logger, BASE_URL
import requests
import json

logger = get_logger()


@dataclass
class ApiHelper(object):
    token:str = "Token 4c5c1417b29500b1c84b8eac99f965eb6ecf2733"


    def __post_request(self, api, data):
        header = {'Content-Type': 'application/json', 'Authorization': self.token}
        resp = requests.post(f'{BASE_URL}{api}', data=json.dumps(data), headers=header)
        if resp.status_code == 200:
            logger.info(f"Data to {api} saved")
        elif resp.status_code == 208:
            logger.error(f"Data {data} already exist")
        else:
            logger.error(f"Fail saving data {resp.status_code}: {resp.text}")

    def save_lagrande(self, data):
        self.__post_request('/api/lagrande/', data)
    
    def save_terminacion(self, data):
        self.__post_request('/api/terminacion2/', data)
