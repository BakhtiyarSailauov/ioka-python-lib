import os

import pytest
from ioka.api import IokaAPI
from ioka.models.customer import Customer


def get_api_key(filename='ioka_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def customer_api():
    api_client = get_api_key()
    api_instance = IokaAPI(api_key=api_client)
    return Customer(api=api_instance)


def test_get_customers(customer_api):
    response = customer_api.get_customers()
    assert type(response) == list


def test_create_customer(customer_api):
    external_id = 'ext_12345'
    email = 'test@example.com'
    phone = '+1234567890'
    response = customer_api.create_customer(external_id, email, phone)
    print(response)
    assert response['status'] == 'success'


def test_get_customer_by_id(customer_api):
    customer_id = 'tN19foY7Nc'
    response = customer_api.get_customer_by_id(customer_id)
    assert response['id'] == customer_id


def test_delete_customer_by_id(customer_api):
    customer_id = 'tN19foY7Ncsadfsaf'
    response = customer_api.delete_customer_by_id(customer_id)
    assert response['status'] == 'success'


def test_get_customer_events(customer_api):
    customer_id = 'tN19foY7Nc'
    response = customer_api.get_customer_events(customer_id)
    assert type(response) == list