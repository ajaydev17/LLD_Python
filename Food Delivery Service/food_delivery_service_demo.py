from food_delivery_service import FoodDeliveryService
from customer import Customer
from restaurant import Restaurant
from menu_item import MenuItem
from delivery_agent import DeliveryAgent
from order import Order, OrderStatus
from order_item import OrderItem


class FoodDeliveryServiceDemo:

    @staticmethod
    def run_demo():
        # create a new food delivery service
        food_delivery_service = FoodDeliveryService.get_instance()

        # register customers
        customer1 = Customer("CUS1", "John", "john.doe@example.com", "555-123-4567")
        customer2 = Customer("CUS2", "Jane", "jane.smith@example.com", "555-234-5678")
        food_delivery_service.register_customer(customer1)
        food_delivery_service.register_customer(customer2)

        # menu items
        menu_item1 = MenuItem("MENU1", "Pizza", "Delicious pizza with tomato sauce", 10.99)
        menu_item2 = MenuItem("MENU2", "Salad", "Fresh green salad with tomatoes", 5.99)
        menu_item3 = MenuItem("MENU3", "Ice Cream", "Sweet and creamy ice cream", 3.99)

        # register restaurants
        restaurant1 = Restaurant("RST1", "Pizza Hut", "123 Main St.", [menu_item1, menu_item2, menu_item3])
        restaurant2 = Restaurant("RST2", "Taco Bell", "456 Elm St.", [menu_item1, menu_item2, menu_item3])
        restaurant3 = Restaurant("RST3", "Burger King", "789 Oak St.", [menu_item1, menu_item2, menu_item3])
        food_delivery_service.register_restaurant(restaurant1)
        food_delivery_service.register_restaurant(restaurant2)
        food_delivery_service.register_restaurant(restaurant3)

        # register delivery agents
        delivery_agent1 = DeliveryAgent("AGT1", "Agent Smith", "555-123-4567")
        delivery_agent2 = DeliveryAgent("AGT2", "Agent Jones", "555-234-5678")
        delivery_agent3 = DeliveryAgent("AGT3", "Agent Lee", "555-345-6789")
        food_delivery_service.register_delivery_agent(delivery_agent1)
        food_delivery_service.register_delivery_agent(delivery_agent2)
        food_delivery_service.register_delivery_agent(delivery_agent3)

        # place orders
        items = [OrderItem(menu_item1, 2), OrderItem(menu_item2, 1), OrderItem(menu_item3, 1)]
        order = food_delivery_service.place_order(customer1.id, restaurant1.id, items)

        if order:
            print(f"Order placed successfully: {order.id}")

        # update order status
        food_delivery_service.update_order_status(order.id, OrderStatus.CONFIRMED)

        # check order details
        print(
            f"Order details: {order.id}, status: {order.status}, items: {[(item.item.name, item.quantity) for item in order.items]}")

        # check available restaurants
        available_restaurants = food_delivery_service.get_available_restaurants()
        print(f"Available restaurants: {[restaurant.name for restaurant in available_restaurants]}")

        # cancel order
        food_delivery_service.cancel_order(order.id)
        print(f"Order cancelled: {order.id}")


if __name__ == "__main__":
    FoodDeliveryServiceDemo.run_demo()