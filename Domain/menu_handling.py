#

class Menu_items:
    def __init__(self):
        pass
    def menu_item(self):

            menu = {"BLACK COFFEE": 50, "GREEN TEA": 50, "GRAVVY MOMOS": 110,"SANDWICH": 70, "BEEF SAUSAGE": 140, "CHICKEN STEAK": 160}
            print(menu)

class Show_menu(Menu_items):
    def __init__(self):
        pass
 
    def show_menu(self):
        while True:
            print('1 - Show menu ')
            print('2 - Add food item ')
            print('3 - Delete food item')
            option=int(input('  Please Choose your option '))

            if option == 1:
                self.menu_item()

            elif option ==2:
                add=Adding_items()
                add.adding_items()

            elif option ==3:
                delete=Delete_iteams()
                delete.delete_iteams()
 
            else:
                 print(" choose correct option please")


class Adding_items(Menu_items):
    def __init__(self):
        pass
    def adding_items(self): 
        self.menu_item()
        menu = {"BLACK COFFEE": 50, "GREEN TEA": 50, "GRAVVY MOMOS": 110,"SANDWICH": 70, "BEEF SAUSAGE": 140, "CHICKEN STEAK": 160}
        name=input('Enter food name you want to add ')
        price=input('Enter food prize ')
        menu[name]=price
        print("food name",menu)
        print("price",price)
        print("successfully added in menu ")
        
        print(menu)     

class Delete_iteams(Menu_items):
    def __init__(self):
        pass
    
    def delete_iteams(self):
        self.menu_item()
        menu = {"BLACK COFFEE": 50, "GREEN TEA": 50, "GRAVVY MOMOS": 110,"SANDWICH": 70, "BEEF SAUSAGE": 140, "CHICKEN STEAK": 160}

        name=input('Enter food name you want to remove ')
        print(name,"SUCCESSFULLY REMOVED ")
        print(menu)
        name=menu.pop(name)
        print("\t\t\t MENU UPDATED",menu)


       

obj= Show_menu()
obj.show_menu()