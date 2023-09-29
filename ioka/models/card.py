class Card:
    def __init__(self, api):
        self.api = api

    def create_binding(self, customer_id, pan, exp, cvc, holder=None):
        endpoint = f"/customers/{customer_id}/bindings"
        payload = {
            "pan": pan,
            "exp": exp,
            "cvc": cvc,
            "holder": holder
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        return self.api._make_request("POST", endpoint, data=payload)

    def get_cards(self, customer_id):
        endpoint = f"/customers/{customer_id}/cards"
        return self.api._make_request("GET", endpoint)

    def get_card_by_id(self, customer_id, card_id):
        endpoint = f"/customers/{customer_id}/cards/{card_id}"
        return self.api._make_request("GET", endpoint)

    def delete_card_by_id(self, customer_id, card_id):
        endpoint = f"/customers/{customer_id}/cards/{card_id}"
        return self.api._make_request("DELETE", endpoint)