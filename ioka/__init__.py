from .api import IokaAPI
from .models.order import Order
from .models.payment import Payment


class IokaAPIClient:
    def __init__(self, api_key):
        self.api = IokaAPI(api_key)
        self.order = Order(self.api)
        self.payment = Payment(self.api)