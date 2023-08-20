from typing import Dict

import requests as r
from requests.auth import HTTPBasicAuth


class CharactersController:
    def __init__(
            self,
            *,
            base_url: str,
            user_login: str,
            user_password: str,
    ) -> None:

        self.url = base_url
        self.password = user_password
        self.login = user_login

    def characters_get(self, auth: bool = True) -> r.Response:
        url = f'{self.url}/characters'
        res = r.get(url=url, auth=HTTPBasicAuth(self.login, self.password)) if auth else r.get(url=url)
        return res

    def character_get(self, name: str, auth: bool = True) -> r.Response:
        url = f'{self.url}/character?name={name}'
        res = r.get(url=url, auth=HTTPBasicAuth(self.login, self.password)) if auth else r.get(url=url)
        return res

    def character_post(self, character: Dict, auth: bool = True) -> r.Response:
        url = f'{self.url}/character'
        res = r.post(
            url=url,
            auth=HTTPBasicAuth(self.login, self.password),
            json=character,
        ) if auth else r.post(url=url)
        return res

    def character_put(self, character: Dict, auth: bool = True) -> r.Response:
        url = f'{self.url}/character'
        res = r.put(url=url, auth=HTTPBasicAuth(self.login, self.password), json=character) if auth else r.put(url=url)
        return res

    def character_delete(self, name: str, auth: bool = True) -> r.Response:
        url = f'{self.url}/character?name={name}'
        res = r.delete(url=url, auth=HTTPBasicAuth(self.login, self.password)) if auth else r.delete(url=url)
        return res

    def reset_post(self, auth: bool = True) -> r.Response:
        url = f'{self.url}/reset/'
        res = r.post(url=url, auth=HTTPBasicAuth(self.login, self.password)) if auth else r.post(url=url)
        return res
