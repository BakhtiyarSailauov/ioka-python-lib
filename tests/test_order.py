import json
import os
import random

import pytest
from ioka.api import IokaAPI
from ioka.models.order import Order


def get_api_key(filename='ioka_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def order_api():
    api_client = get_api_key()
    api_instance = IokaAPI(api_key=api_client)
    return Order(api=api_instance)


def test_create_order(order_api):
    amount = 1000
    currency = "KZT"
    capture_method = "AUTO"
    external_id = random.randrange(1, 174)

    response = order_api.create_order(amount, currency, capture_method, external_id)
    assert int(response['order']['amount']) == amount
    assert int(response['order']['currency']) == currency
    assert int(response['order']['capture_method']) == capture_method
    assert int(response['order']['external_id']) == external_id


def test_get_orders(order_api):
    response = order_api.get_orders(page=1, limit=10)
    assert type(response) == list


def test_get_order_by_id(order_api):
    order_id = 'ord_3rAnDLXFVh'
    response = order_api.get_order_by_id(order_id)
    assert response['id'] == order_id


def test_update_order_by_id(order_api):
    order_id = 'ord_3rAnDLXFVh'
    amount = 2000
    response = order_api.update_order_by_id(order_id, amount)
    assert response['amount'] == amount


def test_capture_order(order_api):
    order_id = 'ord_s63ICHqzsO'
    amount = 1000
    reason = "Capture reason"
    response = order_api.capture_order(order_id, amount, reason)
    assert response['amount'] == amount
    assert response['reason'] == reason


def test_cancel_order(order_api):
    order_id = 'ord_3rAnDLXFVh'
    reason = "Cancel reason"
    response = order_api.cancel_order(order_id, reason)
    assert response['reason'] == reason


def test_get_order_refunds(order_api):
    order_id = 'ord_3rAnDLXFVh'
    response = order_api.get_order_refunds(order_id)
    assert type(response) == list


def test_refund_order(order_api):
    order_id = 'ord_3rAnDLXFVh'
    amount = 500
    reason = "Refund reason"
    rules = ["Rule 1", "Rule 2"]
    positions = [{"name": "Item 1", "quantity": 2}, {"name": "Item 2", "quantity": 1}]
    response = order_api.refund_order(order_id, amount, reason, rules, positions)
    assert response['amount'] == amount
    assert response['reason'] == reason


def test_get_refund_by_id(order_api):
    order_id = 'ord_3rAnDLXFVh'
    refund_id = 'refund_123'
    response = order_api.get_refund_by_id(order_id, refund_id)
    assert response['id'] == refund_id


def test_get_order_events(order_api):
    order_id = 'ord_3rAnDLXFVh'
    response = order_api.get_order_events(order_id)
    assert type(response) == list


def test_get_receipt(order_api):
    order_id = 'ord_3rAnDLXFVh'
    response = order_api.get_receipt(order_id)
    assert 'code' in response