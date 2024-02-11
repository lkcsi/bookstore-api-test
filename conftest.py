import pytest
from client import BookClient, UserClient


@pytest.fixture(scope="function")
def book_payload():
    return {"title": "some_title", "author": "some_author", "quantity": 4}
