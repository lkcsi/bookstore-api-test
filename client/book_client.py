from requests import Response, post, get, patch, delete
import os
import dotenv


class BookClient:

    def __init__(self):
        dotenv.load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.books_endpoint = f'{os.getenv("ENDPOINT")}/api/books'
        self.user_books_endpoint = f'{os.getenv("ENDPOINT")}/api/user-books'

    def create(self, payload: dict) -> Response:
        return post(
            f"{self.books_endpoint}",
            headers={"ApiKey": self.api_key},
            json=payload,
        )

    def get(self, id: str) -> Response:
        return get(
            f"{self.books_endpoint}/{id}",
            headers={"ApiKey": self.api_key},
        )

    def get_all(self) -> Response:
        return get(
            f"{self.books_endpoint}",
            headers={"ApiKey": self.api_key},
        )

    def get_all_user_books(self, username) -> Response:
        return get(
            f"{self.user_books_endpoint}/{username}",
            headers={"ApiKey": self.api_key},
        )

    def delete(self, id: str) -> Response:
        return delete(
            f"{self.books_endpoint}/{id}",
            headers={"ApiKey": self.api_key},
        )

    def checkout(self, username: str, book_id: str) -> Response:
        return patch(
            f"{self.user_books_endpoint}/{username}/checkout/{book_id}",
            headers={"ApiKey": self.api_key},
        )

    def return_book(self, username: str, book_id: str) -> Response:
        return patch(
            f"{self.user_books_endpoint}/{username}/return/{book_id}",
            headers={"ApiKey": self.api_key},
        )
