from requests import Response, post, get, patch, delete
import os
import dotenv


class BookClient:

    def __init__(self):
        dotenv.load_dotenv()
        self.books_endpoint = f'{os.getenv("ENDPOINT")}/books'

    def create(self, token, payload: dict) -> Response:
        return post(
            f"{self.books_endpoint}",
            headers={"Authorization": f"Bearer {token}"},
            json=payload,
        )

    def get(self, token, id: str) -> Response:
        return get(
            f"{self.books_endpoint}/{id}",
            headers={"Authorization": f"Bearer {token}"},
        )

    def get_all(self, token) -> Response:
        return get(
            f"{self.books_endpoint}",
            headers={"Authorization": f"Bearer {token}"},
        )

    def checkout(self, token, id: str) -> Response:
        return patch(
            f"{self.books_endpoint}/{id}/checkout",
            headers={"Authorization": f"Bearer {token}"},
        )

    def delete(self, token: str, id: str) -> Response:
        return delete(
            f"{self.books_endpoint}/{id}",
            headers={"Authorization": f"Bearer {token}"},
        )
