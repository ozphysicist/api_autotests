from typing import Dict

import requests
from requests.auth import HTTPBasicAuth


class Characters:
    def __init__(self) -> None:
        self.host = 'http://rest.test.ivi.ru/v2'
        self.user_password = 'APZrVp83vFNk5F'
        self.user_login = 'zhdanova.o.v@ya.ru'
        self.auth = HTTPBasicAuth('zhdanova.o.v@ya.ru', 'APZrVp83vFNk5F')

    def characters_get(self, authorization: bool = True) -> requests.Response:
        url = f'{self.host}/characters'

        response = requests.get(url=url, auth=self.auth)
        return response

    def character_get(self, name: str) -> requests.Response:
        url = f'{self.host}/character?name={name}'
        response = requests.get(url=url, auth=self.auth)
        return response

    def character_post(self, character: Dict) -> requests.Response:
        url = f'{self.host}/character'
        response = requests.post(url=url, auth=self.auth, json=character)
        return response

    def character_put(self, character: Dict) -> requests.Response:
        url = f'{self.host}/character'
        response = requests.put(url=url, auth=self.auth, json=character)
        return response

    def character_delete(self, name: str) -> requests.Response:
        url = f'{self.host}/character?name={name}'
        response = requests.delete(url=url, auth=self.auth)
        return response

    def reset(self) -> requests.Response:
        url = f'{self.host}/reset'
        response = requests.post(url=url, auth=self.auth)
        return response
