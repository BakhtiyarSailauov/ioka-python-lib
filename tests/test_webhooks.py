import os

import pytest
from ioka.api import IokaAPI
from ioka.models.webhooks import Webhooks


def get_api_key(filename='ioka_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def webhooks_api():
    api_client = get_api_key()
    api_instance = IokaAPI(api_key=api_client)
    return Webhooks(api=api_instance)


def test_get_webhooks(webhooks_api):
    response = webhooks_api.get_webhooks()
    assert type(response) == list


def test_create_webhook(webhooks_api):
    events = ['event1', 'event2']
    response = webhooks_api.create_webhook( events)
    assert response['status'] == 'success'


def test_get_webhook_by_id(webhooks_api):
    webhook_id = 'whk_p6xGBH9Uiw'
    response = webhooks_api.get_webhook_by_id(webhook_id)
    assert response['id'] == webhook_id


def test_delete_webhook_by_id(webhooks_api):
    webhook_id = 'whk_p6xGBH9Uiw'
    response = webhooks_api.delete_webhook_by_id(webhook_id)
    assert response['status'] == 'success'


def test_update_webhook_by_id(webhooks_api):
    webhook_id = 'whk_p6xGBH9Uiw'
    url = 'https://new.webhook.url'
    events = ['new_event1', 'new_event2']
    response = webhooks_api.update_webhook_by_id(webhook_id, url, events)
    assert response['status'] == 'success'
