class MenuItem:
    def __init__(self, menu_item_id: str, name: str, description: str, price: float, availability: bool = True):
        self._id = menu_item_id
        self._name = name
        self._description = description
        self._price = price
        self._availability = availability

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def price(self) -> float:
        return self._price

    @property
    def availability(self) -> bool:
        return self._availability

    @availability.setter
    def availability(self, value: bool) -> None:
        self._availability = value