class Billing:
    def __init__(self):
        pass
    def add_bill(self):
        
            menu = {"BLACK COFFEE": 50, "GREEN TEA": 50, "GRAVVY MOMOS": 110,"SANDWICH": 70,
                    "BEEF SAUSAGE": 140, "CHICKEN STEAK": 160}
            print(menu)
            ordered=input("order here ")
            if ordered in menu:
                print(f'{ordered} order successfully added in cart ')
            else:
                print(" Item not in menu ")

class Order_menu():
     def __init__(self):
          pass
        
     def order_menu(self):
          print('1 - for order something ')
          print('2 - for cancel order    ')
          option=int(input('enter your choice '))
          if option == 1:
               adding=Billing()
               adding.add_bill()
          if option == 2:
               cancelling=Cancel_order()
               cancelling.cancel_order()

class Cancel_order:
     def __init__(self):
          pass
     def cancel_order(self):
           menu = {"BLACK COFFEE": 50, "GREEN TEA": 50, "GRAVVY MOMOS": 110,"SANDWICH": 70,
                    "BEEF SAUSAGE": 140, "CHICKEN STEAK": 160}
           print(menu)
           cancel=input("enter what you want to cancel ")
           if cancel in menu:
                print(f"{cancel}, order cancel successfully")
           else:
                print('Item not in menu ')


    
               
          

        

          
bill=Order_menu()
bill.order_menu() 