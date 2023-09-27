import requests
import logging
import json


class IokaAPIClient:
    def __init__(self, api_key, base_url="https://stage-api.ioka.kz/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger("IokaAPIClient")
        self.logger.setLevel(logging.INFO)

    def _make_request(self, method, endpoint, data=None, headers=None, idempotency_key=None):
        default_headers = {
            "API-KEY": self.api_key,
            "Content-Type": "application/json; charset=utf-8"
        }
        if headers:
            default_headers.update(headers)
        if idempotency_key:
            default_headers['Idempotency-Key'] = idempotency_key

        url = self.base_url + endpoint

        try:
            response = requests.request(method, url, headers=default_headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            self.logger.error(f"HTTP Error: {str(errh)}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request to ioka API failed: {str(e)}")
            raise

    def create_order_with_saved_card(self, amount, customer_id, card_id, idempotency_key=None):
        endpoint = "/orders"
        data = {
            "amount": amount,
            "customer_id": customer_id,
            "card_id": card_id
        }
        return self._make_request("POST", endpoint, data, idempotency_key=idempotency_key)

    def process_payment_with_saved_card(self, order_id, card_id, idempotency_key=None):
        endpoint = f"/orders/{order_id}/payments/card"
        data = {
            "card_id": card_id
        }
        return self._make_request("POST", endpoint, data, idempotency_key=idempotency_key)

    def create_order(self, amount, idempotency_key=None):
        endpoint = "/orders"
        data = {
            "amount": amount
        }
        return self._make_request("POST", endpoint, data, idempotency_key=idempotency_key)

    def get_orders(self, custom_headers=None):
        endpoint = "/orders"
        return self._make_request("GET", endpoint, headers=custom_headers)

    def create_payment(self, data, idempotency_key=None):
        endpoint = "/payments"
        return self._make_request("POST", endpoint, data, idempotency_key=idempotency_key)

    def get_payments(self, custom_headers=None):
        endpoint = "/payments"
        return self._make_request("GET", endpoint, headers=custom_headers)

    def capture_order(self, order_id, idempotency_key=None):
        endpoint = f"/orders/{order_id}/capture"
        return self._make_request("POST", endpoint, idempotency_key=idempotency_key)

    def cancel_order(self, order_id, idempotency_key=None):
        endpoint = f"/orders/{order_id}/cancel"
        return self._make_request("POST", endpoint, idempotency_key=idempotency_key)

    def refund_order(self, order_id, amount, idempotency_key=None):
        endpoint = f"/orders/{order_id}/refund"
        data = {"amount": amount}
        return self._make_request("POST", endpoint, data, idempotency_key=idempotency_key)


if __name__ == "__main__":
    api_key = "your_api_key_here"
    ioka_client = IokaAPIClient(api_key)

    amount = 50000
    order_id = "example_order_id"
    customer_id = "your_customer_id_here"
    card_id = "t3i2tPViLK"

    try:
        order = ioka_client.create_order_with_saved_card(amount, customer_id, card_id)
        print("Order created successfully:")
        print(json.dumps(order, indent=4))

        payment = ioka_client.process_payment_with_saved_card(order['order']['id'], card_id)
        print("Payment processed successfully:")
        print(json.dumps(payment, indent=4))
    except Exception as e:
        print(f"Error: {str(e)}")
