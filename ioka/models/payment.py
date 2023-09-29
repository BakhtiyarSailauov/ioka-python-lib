class Payment:
    def __init__(self, api):
        self.api = api

    def get_payments(self, order_id, page=1, limit=10, to_dt=None, from_dt=None, date_category=None,
                     external_id=None, payment_id=None, pan_first6=None, pan_last4=None, payer_email=None,
                     payer_phone=None, customer_id=None, payment_status=None, payment_system=None,
                     amount_category=None, fixed_amount=None, min_amount=None, max_amount=None):
        endpoint = f"/v2/orders/{order_id}/payments"
        params = {
            "page": page,
            "limit": limit,
            "to_dt": to_dt,
            "from_dt": from_dt,
            "date_category": date_category,
            "external_id": external_id,
            "payment_id": payment_id,
            "pan_first6": pan_first6,
            "pan_last4": pan_last4,
            "payer_email": payer_email,
            "payer_phone": payer_phone,
            "customer_id": customer_id,
            "payment_status": payment_status,
            "payment_system": payment_system,
            "amount_category": amount_category,
            "fixed_amount": fixed_amount,
            "min_amount": min_amount,
            "max_amount": max_amount
        }

        params = {k: v for k, v in params.items() if v is not None}

        return self.api._make_request("GET", endpoint, params=params)

    def create_card_payment(self, order_id, pan, exp, cvc, holder="holder", save=False,
                            email=None, phone=None, card_id=None, fingerprint=None,
                            phone_check_date=None, channel=None):
        endpoint = f"/orders/{order_id}/payments/card"
        payload = {
            "pan": pan,
            "exp": exp,
            "cvc": cvc,
            "holder": holder,
            "save": save,
            "email": email,
            "phone": phone,
            "card_id": card_id,
            "fingerprint": fingerprint,
            "phone_check_date": phone_check_date,
            "channel": channel
        }

        payload = {k: v for k, v in payload.items() if v is not None}

        return self.api._make_request("POST", endpoint, json=payload)

    def get_payments(self, order_id, custom_headers=None):
        endpoint = f"/orders/{order_id}/payments"
        return self.api._make_request("GET", endpoint, headers=custom_headers)

    def create_tool_payment(self, order_id, tool_type, apple_pay=None, google_pay=None):
        endpoint = f"/orders/{order_id}/payments/tool"
        payload = {
            "tool_type": tool_type,
            "apple_pay": apple_pay,
            "google_pay": google_pay
        }

        payload = {k: v for k, v in payload.items() if v is not None}

        return self.api._make_request("POST", endpoint, json=payload)

    def get_payment_by_id(self, order_id, payment_id):
        endpoint = f"/orders/{order_id}/payments/{payment_id}"

        return self.api._make_request("GET", endpoint)
