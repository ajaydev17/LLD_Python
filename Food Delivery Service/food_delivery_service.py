from typing import List, Dict
from uuid import uuid4
from customer import Customer
from restaurant import Restaurant
from order import Order, OrderStatus
from delivery_agent import DeliveryAgent
from menu_item import MenuItem


class FoodDeliveryService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.customers = {}
            cls._instance.restaurants = {}
            cls._instance.orders = {}
            cls._instance.delivery_agents = {}
        return cls._instance

    @staticmethod
    def get_instance():
        if FoodDeliveryService._instance is None:
            FoodDeliveryService()
        return FoodDeliveryService._instance

    def register_customer(self, customer: Customer):
        self.customers[customer.id] = customer

    def register_restaurant(self, restaurant: Restaurant):
        self.restaurants[restaurant.id] = restaurant

    def register_delivery_agent(self, delivery_agent: DeliveryAgent):
        self.delivery_agents[delivery_agent.id] = delivery_agent

    def get_available_restaurants(self) -> List[Restaurant]:
        return [restaurant for restaurant in self.restaurants.values()]

    def get_restaurant_menu(self, restaurant_id: str) -> List[MenuItem]:
        restaurant = self.restaurants.get(restaurant_id)

        if restaurant:
            return restaurant.menu

        return []

    def place_order(self, customer_id: str, restaurant_id: str, items: List[MenuItem]) -> Order:
        customer = self.customers.get(customer_id)
        restaurant = self.restaurants.get(restaurant_id)

        if customer and restaurant:
            order = Order(self.generate_order_id(), customer, restaurant)

            for item in items:
                order.add_item(item)

            self.orders[order.id] = order
            self.notify_restaurant(order)
            return order

        return None

    def update_order_status(self, order_id: str, status: OrderStatus):
        order = self.orders[order_id]

        if order:
            order.status = status
            self.notify_customer(order)

            if status == OrderStatus.CONFIRMED:
                self.assign_delivery_agent(order)

    def cancel_order(self, order_id: str):
        order = self.orders[order_id]

        if order and order.status == OrderStatus.PENDING:
            order.status(OrderStatus.CANCELLED)
            self.notify_customer(order)
            self.notify_restaurant(order)

    def notify_customer(self, order: Order):
        # send notification to the customer about the order status and update
        pass

    def notify_restaurant(self, order: Order):
        # send notification to the restaurant about the new order and order status update
        pass

    def assign_delivery_agent(self, order: Order):
        # assign a delivery agent to the order
        for agent in self.delivery_agents.values():
            if agent.availability:
                agent.availability = False
                order.assign_delivery_agent(agent)
                self.notify_delivery_agent(agent, order)
                break

    def notify_delivery_agent(self, delivery_agent: DeliveryAgent, order: Order):
        # send notification to the delivery agent about the new order and order status update
        pass

    def generate_order_id(self) -> str:
        return "ORD" + str(uuid4().hex[:8].upper())



