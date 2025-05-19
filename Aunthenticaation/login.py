
import json
path = r"C:\repo\Restaurant_management_system\Authentication\login.json"

class Signup:
    def __init__(self):
        pass

    def signup(self):
            listdata=[]
            info = {}
                
            name = input('Please Enter Your Name: ') 
            while name.isdigit():
                 print("please enter a vailed name ")
                 name = input('Please Enter Your Name: ') 

                 
                 print("enter name in a")
            add = input('Please Enter Your Address ')

            id = (input('Please Enter Your email id  '))
            password=input("Create a password ")
            print('You signup up successfully!')
            print(" \tGoing To Login page........\n")
            info = {
                "name": name,
                "id": id,
                "address": add,
                "password": password,
            }
            listdata.append(info)
            with open(path,"w") as file:
                 json.dump(listdata,file,indent=4)
            
           

           


class Option():
    def __init__(self):
        pass

    def option(self):
        print('1 - Staff Login')
        print('2 - Admin Login')
        num = int(input('Please enter your choice: '))
        if num == 1:
            login=Password()
            login.password()
            print("\n! Welcome To Staff section !")
            from Domain.billing import Billing              
          

            
            

        elif num == 2:
            login = Password()
            login.password()
            
            print("\n! Welcome To Admin section !")
            print("1: Menu Handling")
            print("2: Billing Management")
            admin_choice = int(input("Enter your choice: "))

            if admin_choice == 1:
                from Domain.menu_handling import Show_menu
                

            elif admin_choice == 2:
                from Domain.billing import Billing              

            else:
                print("Invalid choice")

        

            
           
        
        else:
            print('Choose a correct option, please ')
            exit()


class Menu(Signup,Option):
    def __init__(self):
        pass

    def menu(self):
        
            print('\t!--- Welcome To Apna Restaurant ---!')
            print('1 - sign up first')
            print('2 - Login')
            print("0 - exit ")
            
            choice = int(input('Please Enter Your Choice: '))
            
            if choice == 1:
                 data=Signup()
                 data.signup()
                 data=Password()
                 data.password()
                
            elif choice == 2:
                 data=Option()
                 data.option()
            elif choice ==0:
                 exit
                
                
            else:
                print('Choose a correct option, please.') 
                exit()



           
class Admin_login:
    def admin_login(self):
            listdata=[]
            info = {}
                
            name = input('Please Enter Your Name: ') 
            id = input('Please Enter Your email id  ')
            add = input('Please Enter Your Address ')
            print('You logined successfully!')
            listdata.append(info)
            print(listdata)



class Password:
    def password(self):
        print("***** Login *****")

        with open(path, "r") as file:
            try:
                logins = json.load(file)
            except json.JSONDecodeError:
                logins = []

            while True:
                email = input("Enter your email: ")
                password = input("Enter your password: ")

                found = False
                for user in logins:
                    if user["id"]==email and user["password"]==password:
                        found = True
                        break

                if found:
                    print("You signed in successfully!")
                    break
                else:
                    print("Wrong email or password\n")
         
info = Menu()
info.menu()
 