import json
import os

path = r"C:\Restaurant_management_system\menu.json"

class MenuItems:
    def __init__(self):
        self.menu = {
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
        def save_menu(self):
            with open(path, 'w') as file:
             json.dump(self.menu, file, indent=4)
    def print_menu(self):
            print("Menu")
            for category, items in self.menu.items():
                print(f"\n{category}:")
            for item in items:
                print(f"{item['item']} - ₹{item['price']}")

            

class Show_menu:
    def __init__(self):
            pass
    def show_menu(self):
       
            print('1 - !-- Show menu --! ')
            print('2 - !-- Add food item --! ')
            print('3 - !-- Delete food item --!')
            option = int(input('Please Choose your option '))

            if option == 1:
                data=MenuItems()
                data.print_menu()
            elif option == 2:
                obj=adding_items()
                obj.add()
            elif option == 3:
                deletion = Remove()
                deletion.remove()
                
            else:
                print("Choose a correct option please")
               
class adding_items(Show_menu):
    def add(self):
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
                name=input("Enter the name of the food item: ")
                price=(input("Enter the price of the food "))
                print(f"{name},{price} successfully add in menu ")
                

            
class Remove(MenuItems):
   
    def remove(self):

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

        name = input('Enter food name you want to remove: ')
        found=False
        for category, items in self.menu.items():
            for food in items:
                if food['item'].lower()== name.lower():
                    items.remove(food)
                    found = True
                    print(f"{name} successfully removed from menu.")
                    break
            
        if not found:
            print("Item not in menu.")

obj=Show_menu()
obj.show_menu() 
