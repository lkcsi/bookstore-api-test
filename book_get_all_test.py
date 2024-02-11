import pytest
from client import BookClient, UserClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()
        self.user_client = UserClient()

    def test_get_all_positive(self, book_payload):
        token = self.user_client.login()

        resp = self.book_client.create(payload=book_payload, token=token)
        assert resp.status_code == 201

        resp = self.book_client.get_all(token=token).json()
        assert isinstance(resp, list)

        assert len(resp) > 0
