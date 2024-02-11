import dotenv
import os
from requests import post


class UserClient:

    def __init__(self):
        dotenv.load_dotenv()
        self.users_endpoint = f'{os.getenv("ENDPOINT")}/users'
        self.token = ""

    def login(self) -> str:
        if not self.token:
            user = os.getenv("BOOK_USER")
            pwd = os.getenv("PASSWORD")

            resp = post(
                f"{self.users_endpoint}/login", json={"username": user, "password": pwd}
            )

            self.token = resp.json()["access_token"]

        return self.token
