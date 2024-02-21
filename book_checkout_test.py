import pytest
from client import BookClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()
        self.username = "test"

    def test_checkout_out_of_stock(self):

        payload = {"title": "book", "author": "some_author", "quantity": 0}
        create_resp = self.book_client.create(payload=payload)
        assert create_resp.status_code == 201

        id = create_resp.json()["id"]
        patch_resp = self.book_client.checkout(username=self.username, book_id=id)
        assert patch_resp.status_code == 400
        assert "out of stock" in patch_resp.json()["error"]

    def test_checkout_positive(self, book_payload):

        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201

        id = resp.json()["id"]
        resp = self.book_client.checkout(username=self.username, book_id=id)
        assert resp.status_code == 202
        assert resp.json()["quantity"] == 3

    def test_checkout_same_multiple_times(self, book_payload):

        resp = self.book_client.create(payload=book_payload)
        assert resp.status_code == 201

        id = resp.json()["id"]
        resp = self.book_client.checkout(username=self.username, book_id=id)
        assert resp.status_code == 202

        resp = self.book_client.checkout(username=self.username, book_id=id)
        assert resp.status_code == 400
        assert (
            resp.json()["error"]
            == f"book {id} has already been checked out by {self.username}"
        )

    def test_checkout_multiple_books(self, book_payload):

        ids = []
        for _ in range(2):
            resp = self.book_client.create(payload=book_payload)
            assert resp.status_code == 201

            id = resp.json()["id"]
            ids.append(id)

            resp = self.book_client.checkout(username=self.username, book_id=id)
            assert resp.status_code == 202

        resp = self.book_client.get_all_user_books(self.username)
        assert resp.status_code == 200

        resp = resp.json()
        assert isinstance(resp, list)

        resp = [book["book-id"] for book in resp]
        assert set(ids).issubset(set(resp))
