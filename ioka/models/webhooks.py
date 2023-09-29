class Webhooks:
    def __init__(self, api):
        self.api = api

    def get_webhooks(self):
        endpoint = "/webhooks"
        return self.api._make_request("GET", endpoint)

    def create_webhook(self, url, events):
        endpoint = "/webhooks"
        payload = {
            "url": url,
            "events": events
        }
        return self.api._make_request("POST", endpoint, data=payload)

    def get_webhook_by_id(self, webhook_id):
        endpoint = f"/webhooks/{webhook_id}"
        return self.api._make_request("GET", endpoint)

    def delete_webhook_by_id(self, webhook_id):
        endpoint = f"/webhooks/{webhook_id}"
        return self.api._make_request("DELETE", endpoint)

    def update_webhook_by_id(self, webhook_id, url, events):
        endpoint = f"/webhooks/{webhook_id}"
        payload = {
            "url": url,
            "events": events
        }
        return self.api._make_request("PATCH", endpoint, data=payload)