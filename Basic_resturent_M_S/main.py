import json

class Restaurant:
    def __init__(self):
        self.orders = self.load_orders()

    def save_orders(self):
        with open('orders.json', 'w') as f:
            json.dump(self.orders, f)

    def load_orders(self):
        try:
            with open('orders.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def order_info(self):
        if not self.orders:
            print("No orders have been placed yet.")
        else:
            for index, order in enumerate(self.orders, start=1):
                print(f"Order {index}: {order}")

    def take_order(self, name, mob, add, order):
        new_order = {
            "NAME": name,
            "MOBILE_NO": mob,
            "ADDRESS": add,
            "ORDER": order
        }
        self.orders.append(new_order)
        self.save_orders()
        print("Order placed successfully!")
        print(new_order)

    def update_order(self, order_index, name, mob, add, order):
        if 0 <= order_index < len(self.orders):
            self.orders[order_index] = {
                "NAME": name,
                "MOBILE_NO": mob,
                "ADDRESS": add,
                "ORDER": order
            }
            self.save_orders()
            print("Order updated successfully!")
        else:
            print("Invalid order index.")

    def delete_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            self.orders.pop(order_index)
            self.save_orders()
            print("Order deleted successfully!")
        else:
            print("Invalid order index.")

    def search_order(self, keyword):
        results = [order for order in self.orders if keyword in order.values()]
        if results:
            for index, order in enumerate(results, start=1):
                print(f"Result {index}: {order}")
        else:
            print("No matching orders found.")

if __name__ == "__main__":
    restaurant = Restaurant()
    
    while True:
        print("\nWELCOME TO THE RESTAURANT ORDER SYSTEM")
        print("PRESS 1 TO PLACE AN ORDER")
        print("PRESS 2 TO VIEW ALL ORDERS")
        print("PRESS 3 TO UPDATE AN ORDER")
        print("PRESS 4 TO DELETE AN ORDER")
        print("PRESS 5 TO SEARCH FOR AN ORDER")
        print("PRESS 6 TO EXIT")
        choice = input("CHOOSE AN OPTION: ")

        if choice == "1":
            name = input("PLEASE ENTER YOUR NAME: ")
            mob = input("PLEASE ENTER YOUR MOBILE NUMBER: ")
            add = input("PLEASE ENTER YOUR ADDRESS: ")
            order = input("PLEASE ENTER YOUR ORDER: ")
            restaurant.take_order(name, mob, add, order)
        elif choice == "2":
            restaurant.order_info()
        elif choice == "3":
            try:
                order_index = int(input("ENTER THE ORDER NUMBER TO UPDATE: ")) - 1
                name = input("PLEASE ENTER YOUR NAME: ")
                mob = input("PLEASE ENTER YOUR MOBILE NUMBER: ")
                add = input("PLEASE ENTER YOUR ADDRESS: ")
                order = input("PLEASE ENTER YOUR ORDER: ")
                restaurant.update_order(order_index, name, mob, add, order)
            except ValueError:
                print("Invalid input. Please enter a valid order number.")
        elif choice == "4":
            try:
                order_index = int(input("ENTER THE ORDER NUMBER TO DELETE: ")) - 1
                restaurant.delete_order(order_index)
            except ValueError:
                print("Invalid input. Please enter a valid order number.")
        elif choice == "5":
            keyword = input("ENTER NAME OR MOBILE NUMBER TO SEARCH: ")
            restaurant.search_order(keyword)
        elif choice == "6":
            print("Thank you for using the restaurant order system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
