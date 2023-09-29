# Библиотека Ioka для Python

`ioka-python-lib` — это библиотека на Python для взаимодействия с API Ioka. Она предоставляет удобный интерфейс для выполнения API-вызовов и управления ресурсами, такими как клиенты, карты, заказы, платежи и веб-хуки.

## Установка

Установите `ioka-python-lib` с помощью pip:

```bash
pip install ioka-python-lib
```
# Конфигурация
Перед выполнением каких-либо API-вызовов настройте библиотеку с вашим API-ключом:
```python
from ioka import IokaAPI

api = IokaAPI(api_key='ваш-api-ключ-здесь')
```

# Использование
Вот несколько примеров того, как можно использовать ioka-python-lib:

## Управление клиентами
```python
from ioka import Customer

# Создание нового клиента
customer = api.create_customer(external_id='123', email='user@example.com', phone='+1234567890')

# Получение списка клиентов
customers = api.get_customers()
```
## Управление картами

```python
from ioka import Card

# Создание привязки карты
card = api.create_binding(customer_id='123', pan='4111111111111111', exp='12/23', cvc='123')

# Получение списка карт клиента
cards = api.get_cards(customer_id='123')
```

## Документация
Для более подробной информации ознакомьтесь с [документацией.](docs/index.md)