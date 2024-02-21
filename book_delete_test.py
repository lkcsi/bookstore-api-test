import pytest
from client import BookClient, UserClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()

    def test_delete_positive(self, book_payload):
        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201

        data = resp.json()
        book_payload["id"] = data["id"]
        assert data == book_payload

        resp = self.book_client.delete(id=data["id"])
        assert resp.status_code == 204

    def test_delete_not_exist(self):
        resp = self.book_client.delete(id="test_id")
        assert resp.status_code == 404
        assert "test_id is not found" in resp.json()["error"]
