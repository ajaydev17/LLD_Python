class DeliveryAgent:
    def __init__(self, agent_id: str, name: str, phone: str, availability: bool = True):
        self._id = agent_id
        self._name = name
        self._phone = phone
        self._availability = availability

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def availability(self) -> bool:
        return self._availability

    @availability.setter
    def availability(self, value: bool):
        self._availability = value