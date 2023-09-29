import requests
import logging


class IokaAPI:
    def __init__(self, api_key, base_url="https://stage-api.ioka.kz/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger("IokaAPIClient")
        self.logger.setLevel(logging.INFO)

    def _make_request(self, method, endpoint, data=None, headers=None, idempotency_key=None, json=None, params=None):
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
            response = requests.request(method, url, headers=default_headers, data=data, json=json, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            try:
                error_response = response.json()
                self.logger.error(f"HTTP Error: {response.status_code} - {error_response}")
            except:
                self.logger.error(f"HTTP Error: {str(errh)}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request to ioka API failed: {str(e)}")
            raise

        @staticmethod
        def format_date(date_obj):
            return date_obj.strftime("%Y-%m-%dT%H:%M:%S")
