import pytest
from client import BookClient, UserClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()

    def test_get_all_positive(self, book_payload):
        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201

        resp = self.book_client.get_all().json()
        assert isinstance(resp, list)

        assert len(resp) > 0
