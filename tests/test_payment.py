import os

import pytest
from ioka.api import IokaAPI
from ioka.models.payment import Payment


def get_api_key(filename='ioka_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def payment_api():
    api_client = get_api_key()
    api_instance = IokaAPI(api_key=api_client)
    return Payment(api=api_instance)


def test_get_payments(payment_api):
    order_id = 'shp_SNL708X0PI'
    response = payment_api.get_payments(order_id)
    assert type(response) == list


def test_get_payments(payment_api):
    order_id = "ord_78fRDy8lel"
    custom_headers = {"Custom-Header": "HeaderValue"}

    response = payment_api.get_payments(order_id, custom_headers)
    assert type(response) == list


def test_create_card_payment(payment_api):
    order_id = 'ord_3rAnDLXFVh'
    pan = '4111111111111111'
    exp = '1222'
    cvc = '123'
    response = payment_api.create_card_payment(order_id, pan, exp, cvc)
    assert response['status'] == 'success'


def test_create_tool_payment(payment_api):
    order_id = 'ord_3rAnDLXFVh'
    tool_type = 'APPLE_PAY'
    apple_pay_data = {
        'version': 'EC_v1',
        'data': '...',
        'signature': '...',
        'header': {
            'ephemeralPublicKey': '...',
            'publicKeyHash': '...',
            'transactionId': '...'
        }
    }
    response = payment_api.create_tool_payment(order_id, tool_type, apple_pay=apple_pay_data)
    assert response['status'] == 'success'


def test_get_payment_by_id(payment_api):
    order_id = 'ord_3rAnDLXFVh'
    payment_id = 'pay_mNwerLHocZ'
    response = payment_api.get_payment_by_id(order_id, payment_id)
    print(response)
    assert response['order_id'] == order_id





