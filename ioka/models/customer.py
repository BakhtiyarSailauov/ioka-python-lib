class Customer:
    def __init__(self, api):
        self.api = api

    def get_customers(self, limit=10, page=1, to_dt=None, from_dt=None, date_category=None,
                      customer_id=None, external_id=None, status=None):
        endpoint = '/customers'
        params = {
            'limit': limit,
            'page': page,
            'to_dt': to_dt,
            'from_dt': from_dt,
            'date_category': date_category,
            'customer_id': customer_id,
            'external_id': external_id,
            'status': status
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self.api._make_request("GET", endpoint, params=params)

    def create_customer(self, external_id, email, phone, fingerprint=None,
                        phone_check_date=None, channel=None):
        endpoint = '/customers'
        data = {
            'external_id': external_id,
            'email': email,
            'phone': phone,
            'fingerprint': fingerprint,
            'phone_check_date': phone_check_date,
            'channel': channel
        }
        data = {k: v for k, v in data.items() if v is not None}
        return self.api._make_request("POST", endpoint, data=data)

    def get_customer_by_id(self, customer_id):
        endpoint = f'/customers/{customer_id}'
        return self.api._make_request("GET", endpoint)

    def delete_customer_by_id(self, customer_id):
        endpoint = f'/customers/{customer_id}'
        return self.api._make_request("DELETE", endpoint)

    def get_customer_events(self, customer_id):
        endpoint = f'/customers/{customer_id}/events'
        return self.api._make_request("GET", endpoint)
