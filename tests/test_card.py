import os

import pytest
from ioka.api import IokaAPI
from ioka.models.card import Card


def get_api_key(filename='ioka_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def card_api():
    api_client = get_api_key()
    api_instance = IokaAPI(api_key=api_client)
    return Card(api=api_instance)


def test_create_binding(card_api):
    customer_id = 'mNqK04RThO'
    pan = '4111111111111111'
    exp = '1222'
    cvc = '123'
    response = card_api.create_binding(customer_id, pan, exp, cvc)
    assert response['status'] == 'success'


def test_get_cards(card_api):
    customer_id = 'mNqK04RThO'
    response = card_api.get_cards(customer_id)
    assert type(response) == list


def test_get_card_by_id(card_api):
    customer_id = 'mNqK04RThO'
    card_id = 'card_12345'
    response = card_api.get_card_by_id(customer_id, card_id)
    assert response['id'] == card_id


def test_delete_card_by_id(card_api):
    customer_id = 'mNqK04RThO'
    card_id = 'card_12345'
    response = card_api.delete_card_by_id(customer_id, card_id)
    assert response['status'] == 'success'
