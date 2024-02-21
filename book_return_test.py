import pytest
from client import BookClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()
        self.username = "test"

    def test_return_positive(self, book_payload):

        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201

        id = resp.json()["id"]
        resp = self.book_client.checkout(username=self.username, book_id=id)
        assert resp.status_code == 202
        assert resp.json()["quantity"] == 3

        resp = self.book_client.return_book(username=self.username, book_id=id)
        assert resp.status_code == 202

        resp = self.book_client.get(id)
        assert resp.json()["quantity"] == 4

    def test_return_without_checkout(self, book_payload):

        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201
        id = resp.json()["id"]

        resp = self.book_client.return_book(username=self.username, book_id=id)
        assert resp.status_code == 404
        assert (
            resp.json()["error"]
            == f"book with id: {id} is not found in {self.username}'s books"
        )
