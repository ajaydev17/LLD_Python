from enum import Enum
from typing import List

class OrderStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    PREPARING = "PREPARING"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class Order:
    def __init__(self, order_id: str, customer, restaurant):
        self._id = order_id
        self._customer = customer
        self._restaurant = restaurant
        self._items = []
        self._status = OrderStatus.PENDING
        self._delivery_agent = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def status(self) -> OrderStatus:
        return self._status

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    @status.setter
    def status(self, value: OrderStatus) -> None:
        self._status = value

    def assign_delivery_agent(self, delivery_agent):
        self._delivery_agent = delivery_agent