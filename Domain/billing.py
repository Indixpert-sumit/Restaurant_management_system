import json

menu = {
    "breakfast": [
        {"item": "Pancakes", "price": 120},
        {"item": "Omelette", "price": 100},
        {"item": "Idli Sambhar", "price": 80},
        {"item": "Paratha", "price": 90}
    ],
    "lunch": [
        {"item": "Paneer Butter Masala", "price": 180},
        {"item": "Chicken Biryani", "price": 200},
        {"item": "Veg Thali", "price": 150},
        {"item": "Dal Makhani", "price": 130}
    ],
    "dinner": [
        {"item": "Butter Naan", "price": 40},
        {"item": "Mutton Rogan Josh", "price": 220},
        {"item": "Kadhai Paneer", "price": 170},
        {"item": "Jeera Rice", "price": 90}
    ],
    "Water and Soft Drinks": [
        {"item": "Mineral Water", "price": 20},
        {"item": "Masala Chai", "price": 30},
        {"item": "Lassi", "price": 50},
        {"item": "Cold Drink", "price": 40}
    ]
}

class Billing:
    def __init__(self):
        self.order = []
        self.total = 0

    def add_bill(self):
        print("Menu:")
        for category, items in menu.items():
            print(f"\n{category}:")
            for item in items:
                print(f"{item['item']} - ₹{item['price']}")

        while True:
            order_item = input("\nEnter the item you want to order ( type done to show bill ): ").strip()
            if order_item.lower() == 'done':
                break
            found = False
            for category, items in menu.items():
                for item in items:
                    if item['item'].lower() == order_item.lower():
                        self.order.append(item)
                        self.total += item['price']
                        print(f"{item['item']} added to your order.")
                        found = True
                        break
                if found:
                    break
            if not found:
                print("Item not found in the menu. Please try again.")

    def display_bill(self):
        if self.order:
            print("\nYour Order:")
            for item in self.order:
                print(f"{item['item']} - ₹{item['price']}")
            print(f"\nTotal Amount: ₹{self.total}")
        else:
            print("No items ordered.")

class OrderMenu:
    def __init__(self):
        self.billing = Billing()

    def order_menu(self):
        while True:
            print("\n1 - Order Food")
            print("2 - Cancel Order")
            print("0 - Exit")
            option = input("Enter your choice: ").strip()
            if option == '1':
                self.billing.add_bill()
                self.billing.display_bill()
            elif option == '2':
                self.billing = Billing() 
                print("Your order has been canceled.")
            elif option == '0':
                print("exiting....!")
                break
            else:
                print("Invalid choice ")

order_system = OrderMenu()
order_system.order_menu()
