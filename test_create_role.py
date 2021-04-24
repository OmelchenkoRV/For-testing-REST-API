import pytest
import requests


@pytest.fixture()
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com/'


@pytest.fixture(base_url)
def init_book():
    book_data = {'title': 'new', 'author': 'new'}
    resp = requests.post(f'{base_url}/books', data=book_data)
    book = resp.json()
    yield book
    resp = requests.delete(f'{base_url}/books/{book["id"]}')


def test_create_role(init_book, base_url):
    assert init_book['id'] == 0
