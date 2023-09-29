class Order:
    def __init__(self, api):
        self.api = api

    def create_order(self, amount, currency="KZT", capture_method="AUTO", external_id=None,
                     description=None, mcc=None, extra_info=None, attempts=10,
                     due_date=None, customer_id=None, card_id=None, back_url=None,
                     success_url=None, failure_url=None, template=None):
        endpoint = "/orders"
        payload = {
            "amount": amount,
            "currency": currency,
            "capture_method": capture_method,
            "external_id": external_id,
            "description": description,
            "mcc": mcc,
            "extra_info": extra_info,
            "attempts": attempts,
            "due_date": due_date,
            "customer_id": customer_id,
            "card_id": card_id,
            "back_url": back_url,
            "success_url": success_url,
            "failure_url": failure_url,
            "template": template
        }

        payload = {k: v for k, v in payload.items() if v is not None}

        return self.api._make_request("POST", endpoint, json=payload)

    def get_orders(self, page=1, limit=10, to_dt=None, from_dt=None, date_category=None,
                   order_id=None, external_id=None, order_status=None, amount_category=None,
                   fixed_amount=None, min_amount=None, max_amount=None):
        endpoint = "/orders"
        params = {
            "page": page,
            "limit": limit,
            "to_dt": to_dt,
            "from_dt": from_dt,
            "date_category": date_category,
            "order_id": order_id,
            "external_id": external_id,
            "order_status": order_status,
            "amount_category": amount_category,
            "fixed_amount": fixed_amount,
            "min_amount": min_amount,
            "max_amount": max_amount
        }

        params = {k: v for k, v in params.items() if v is not None}

        return self.api._make_request("GET", endpoint, params=params)

    def get_order_by_id(self, order_id):
        endpoint = f"/orders/{order_id}"
        return self.api._make_request("GET", endpoint)

    def update_order_by_id(self, order_id, amount):
        endpoint = f"/orders/{order_id}"
        payload = {
            "amount": amount
        }
        return self.api._make_request("PATCH", endpoint, json=payload)

    def capture_order(self, order_id, amount, reason):
        endpoint = f"/orders/{order_id}/capture"
        payload = {
            "amount": amount,
            "reason": reason
        }
        return self.api._make_request("POST", endpoint, json=payload)

    def cancel_order(self, order_id, reason):
        endpoint = f"/orders/{order_id}/cancel"
        payload = {
            "reason": reason
        }
        return self.api._make_request("POST", endpoint, json=payload)

    def get_order_refunds(self, order_id):
        endpoint = f"/orders/{order_id}/refunds"
        return self.api._make_request("GET", endpoint)

    def refund_order(self, order_id, amount, reason, rules, positions):
        endpoint = f"/orders/{order_id}/refunds"
        payload = {
            "amount": amount,
            "reason": reason,
            "rules": rules,
            "positions": positions
        }
        return self.api._make_request("POST", endpoint, json=payload)

    def get_refund_by_id(self, order_id, refund_id):
        endpoint = f"/orders/{order_id}/refunds/{refund_id}"
        return self.api._make_request("GET", endpoint)

    def get_order_events(self, order_id):
        endpoint = f"/orders/{order_id}/events"
        return self.api._make_request("GET", endpoint)

    def get_receipt(self, order_id):
        endpoint = f"/orders/{order_id}/receipt"
        return self.api._make_request("GET", endpoint)