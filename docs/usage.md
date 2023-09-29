# Использование

Примеры использования основных классов и методов библиотеки.

## Создание заказа

```python
from ioka.models.order import Order

order = Order(api_client)
response = order.create_order(amount=1000)
```

Получение информации о заказе
```python
response = order.get_order_by_id(order_id="your-order-id-here")
```

## Работа с платежами
 Для работы с платежами используется класс Payment:

## Создание платежа по карте

```python
from ioka.models.payment import Payment

payment = Payment(api_client)
response = payment.create_card_payment(order_id="your-order-id-here", pan="1234567812345678", exp="12/23", cvc="123")
```

## Работа с веб-хуками
Для работы с веб-хуками используется класс Webhooks:

## Создание веб-хука

from ioka.models.webhook import Webhooks
```python

webhooks = Webhooks(api_client)
response = webhooks.create_webhook(url="https://your-webhook-url-here", events=["event1", "event2"])
