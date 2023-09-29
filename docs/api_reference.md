# Модели
Библиотека включает в себя модели для работы с различными объектами API, такими как заказы, платежи, клиенты, карты и веб-хуки.

# API Reference

##  Класс `Card`

 Класс `Card` предоставляет методы для работы с карточками клиентов.

### Методы

- `__init__(self, api)`
  - IИнициализация объекта класса  `Card`.
- `create_binding(self, customer_id, pan, exp, cvc, holder=None)`
  - Создание привязки карты к клиенту.
- `get_cards(self, customer_id)`
  - Получение списка карт клиента.
- `get_card_by_id(self, customer_id, card_id)`
  - Получение списка карт клиента.
- `delete_card_by_id(self, customer_id, card_id)`
  - Удаление карты по  ID.

## Класс `Customer` 

 `Customer` предоставляет методы для работы с клиентами.

### Методы

- `__init__(self, api)`
  - Инициализация объекта класса `Customer`
- `get_customers(self, limit=10, page=1, to_dt=None, from_dt=None, date_category=None, customer_id=None, external_id=None, status=None)`
  - Получение списка клиентов с возможностью фильтрации и пагинации
- `create_customer(self, external_id, email, phone, fingerprint=None, phone_check_date=None, channel=None)`
  - Создание нового клиента.
- `get_customer_by_id(self, customer_id)`
  - Получение информации о клиенте по ID.
- `delete_customer_by_id(self, customer_id)`
  - Удаление клиента по ID.
- `get_customer_events(self, customer_id)`
  - Получение списка событий клиента.



## Класс `Order`

Класс `Order` предоставляет методы для работы с заказами.

### Методы

- `create_order(...)`
  - Создание нового заказа.
- `get_orders(...)`
  - Получение списка заказов с возможностью фильтрации и пагинации.
- `get_order_by_id(order_id)`
  - Получение информации о заказе по ID.
- `update_order_by_id(order_id, amount)`
  - Обновление суммы заказа по ID.
- `capture_order(order_id, amount, reason)`
  - Проведение заказа по ID.
- `cancel_order(order_id, reason)`
  - Отмена заказа по ID.
- `get_order_refunds(order_id)`
  - Получение списка возвратов по заказу.
- `refund_order(order_id, amount, reason, rules, positions)`
  - Создание возврата по заказу.
- `get_refund_by_id(order_id, refund_id)`
  - Получение информации о возврате по ID.
- `get_order_events(order_id)`
  - Получение списка событий по заказу.
- `get_receipt(order_id)`
  - Получение чека по заказу.

## Класс `Payment`

Класс `Payment` предоставляет методы для работы с платежами.

### Методы

- `get_payments(order_id, ...)`
  - Получение списка платежей по заказу.
- `create_card_payment(order_id, ...)`
  - Создание платежа по карте по заказу.
- `create_tool_payment(order_id, tool_type, apple_pay=None, google_pay=None)`
  - Создание платежа по инструменту платежа по заказу.
- `get_payment_by_id(order_id, payment_id)`
  - Получение информации о платеже по ID.

## Класс `Webhooks`

Класс `Webhooks` предоставляет методы для работы с веб-хуками.

### Методы

- `get_webhooks()`
  - Получение списка веб-хуков.
- `create_webhook(url, events)`
  - Создание нового веб-хука.
- `get_webhook_by_id(webhook_id)`
  - Получение информации о веб-хуке по ID.
- `delete_webhook_by_id(webhook_id)`
  - Удаление веб-хука по ID.
- `update_webhook_by_id(webhook_id, url, events)`
  - Обновление веб-хука по ID.

