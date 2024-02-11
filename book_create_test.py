import pytest
from client import BookClient, UserClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()
        self.user_client = UserClient()

    def test_create_positive(self, book_payload):
        token = self.user_client.login()

        create_resp = self.book_client.create(payload=book_payload, token=token)
        assert create_resp.status_code == 201

        data = create_resp.json()
        book_payload["id"] = data["id"]
        assert data == book_payload

        get_resp = self.book_client.get(id=data["id"], token=token)
        assert get_resp.status_code == 200
        assert get_resp.json() == book_payload

    def test_create_missing_title(self, book_payload):
        token = self.user_client.login()

        book_payload["title"] = ""

        create_resp = self.book_client.create(payload=book_payload, token=token)
        assert create_resp.status_code == 400
        assert "Title field is mandatory" in create_resp.json()["error"]

    def test_create_missing_author(self, book_payload):
        token = self.user_client.login()

        book_payload["author"] = ""

        create_resp = self.book_client.create(payload=book_payload, token=token)
        assert create_resp.status_code == 400
        assert "Author field is mandatory" in create_resp.json()["error"]
