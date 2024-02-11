import pytest
from client import BookClient, UserClient


class TestBookApi:

    def setup_class(self):
        self.book_client = BookClient()
        self.user_client = UserClient()

    def test_checkout_out_of_stock(self):
        token = self.user_client.login()

        payload = {"title": "book", "author": "some_author", "quantity": 0}
        create_resp = self.book_client.create(payload=payload, token=token)
        assert create_resp.status_code == 201

        id = create_resp.json()["id"]
        patch_resp = self.book_client.checkout(id=id, token=token)
        assert patch_resp.status_code == 400
        assert "out of stock" in patch_resp.json()["error"]

    def test_checkout_positive(self, book_payload):
        token = self.user_client.login()

        create_resp = self.book_client.create(payload=book_payload, token=token)
        assert create_resp.status_code == 201

        id = create_resp.json()["id"]
        patch_resp = self.book_client.checkout(id=id, token=token)
        assert patch_resp.status_code == 202
        assert patch_resp.json()["quantity"] == 3
