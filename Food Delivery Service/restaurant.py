from typing import List
from menu_item import MenuItem

class Restaurant:
    def __init__(self, restaurant_id: str, name: str, address: str, menu: List[MenuItem]):
        self._id = restaurant_id
        self._name = name
        self._address = address
        self._menu = menu

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> str:
        return self._address

    @property
    def menu(self) -> list:
        return self._menu

    def add_menu_item(self, menu_item: MenuItem) -> None:
        self._menu.append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem) -> None:
        self._menu.remove(menu_item)